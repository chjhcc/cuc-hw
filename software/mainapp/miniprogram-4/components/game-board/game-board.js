import { GameManager } from '../../utils/gameManager';

Component({
  properties: {
    boardSize: {
      type: Number,
      value: 800
    }
  },
  
  data: {
    updateTimer: null,
    // 游戏格子配置
    squares: [
      // 底部一行
      { id: 0, type: 'start', name: '起点', position: [0, 7] },
      { id: 1, type: 'property', name: '北京路', price: 1000, position: [1, 7] },
      { id: 2, type: 'chance', name: '机会', position: [2, 7] },
      { id: 3, type: 'property', name: '上海路', price: 1500, position: [3, 7] },
      { id: 4, type: 'property', name: '南京路', price: 2000, position: [4, 7] },
      { id: 5, type: 'property', name: '杭州路', price: 1800, position: [5, 7] },
      { id: 6, type: 'chance', name: '命运', position: [6, 7] },
      { id: 7, type: 'property', name: '成都路', price: 2200, position: [7, 7] },
      // 右侧一列
      { id: 8, type: 'property', name: '重庆路', price: 2400, position: [7, 6] },
      { id: 9, type: 'property', name: '武汉路', price: 2600, position: [7, 5] },
      { id: 10, type: 'chance', name: '机会', position: [7, 4] },
      { id: 11, type: 'property', name: '广州路', price: 2800, position: [7, 3] },
      { id: 12, type: 'property', name: '深圳路', price: 3000, position: [7, 2] },
      { id: 13, type: 'property', name: '珠海路', price: 3100, position: [7, 1] },
      // 顶部一行（从右到左）
      { id: 14, type: 'property', name: '天津路', price: 3200, position: [7, 0] },
      { id: 15, type: 'chance', name: '命运', position: [6, 0] },
      { id: 16, type: 'property', name: '西安路', price: 3400, position: [5, 0] },
      { id: 17, type: 'property', name: '长沙路', price: 3600, position: [4, 0] },
      { id: 18, type: 'property', name: '南宁路', price: 3800, position: [3, 0] },
      { id: 19, type: 'chance', name: '机会', position: [2, 0] },
      { id: 20, type: 'property', name: '昆明路', price: 4000, position: [1, 0] },
      { id: 21, type: 'property', name: '厦门路', price: 4200, position: [0, 0] },
      // 左侧一列（从上到下）
      { id: 22, type: 'property', name: '青岛路', price: 4400, position: [0, 1] },
      { id: 23, type: 'chance', name: '命运', position: [0, 2] },
      { id: 24, type: 'property', name: '大连路', price: 4600, position: [0, 3] },
      { id: 25, type: 'property', name: '济南路', price: 4800, position: [0, 4] },
      { id: 26, type: 'property', name: '郑州路', price: 5000, position: [0, 5] },
      { id: 27, type: 'chance', name: '机会', position: [0, 6] }
    ],
    gameState: null,
    showTurnTip: false,
    canRollDice: true,
    scoreLogs: []
  },

  lifetimes: {
    attached() {
      this.initBoard();
      this.initGame();
    }
  },

  methods: {
    initBoard() {
      // 计算每个格子的具体位置
      const gridSize = this.data.boardSize / 8; // 8x8 的棋盘
      const offset = 0; // 移除偏移量
      let squares = this.data.squares.map(square => {
        // 根据 id 计算具体位置
        const x = square.position[0] * gridSize + offset;
        const y = square.position[1] * gridSize + offset;
        // 如果有所有者，添加颜色
        let ownerColor = '#fff';
        if (square.ownerId && this.data.gameState) {
          const owner = this.data.gameState.players.find(p => p.id === square.ownerId);
          if (owner) {
            ownerColor = owner.color + '66';
          }
        }
        return { ...square, x, y, ownerColor };
      });
      
      this.setData({ squares });
    },

    initGame() {
      const gameState = GameManager.initGameState();
      // 先设置初始状态
      this.setData({ gameState }, () => {
        // 显示游戏规则
        wx.showModal({
          title: '游戏规则',
          content: '1. 每位玩家初始资金15000分\n2. 按掷骰子点数决定行动顺序\n3. 第一个达到25000分的玩家获胜\n\n准备好了吗？',
          showCancel: false,
          success: () => {
            // 再进行掷骰子决定顺序
            this.determinePlayOrder();
          }
        });
      });
    },

    // 决定玩家顺序
    determinePlayOrder() {
      let { gameState } = this.data;
      if (!gameState) {
        console.error('游戏状态未初始化');
        return;
      }
      let playerRolls = [];

      const rollForOrder = (index) => {
        if (index >= gameState.players.length) {
          // 所有玩家都掷完骰子后，按点数排序
          playerRolls.sort((a, b) => b.number - a.number);
          
          // 重新排序玩家数组
          gameState.players = playerRolls.map(roll => {
            return gameState.players.find(p => p.id === roll.playerId);
          });
          
          // 记录顺序确定的日志
          playerRolls.forEach((roll, idx) => {
            const player = gameState.players.find(p => p.id === roll.playerId);
            this.addScoreLog(
              player.name,
              0,
              `掷出 ${roll.number} 点，确定为第 ${idx + 1} 位`
            );
          });
          
          // 更新游戏状态
          this.updateGameState(gameState);
          
          // 触发父组件更新
          this.triggerEvent('stateUpdate', { gameState });
          
          // 显示游戏开始提示
          wx.showModal({
            title: '游戏开始',
            content: `决定顺序：\n${playerRolls.map(roll => 
              `${gameState.players.find(p => p.id === roll.playerId).name}: ${roll.number}点`
            ).join('\n')}\n\n${gameState.players[0].name}先开始`,
            showCancel: false,
            success: () => {
              this.showNextPlayerTurn(gameState.players[0]);
            }
          });
          return;
        }

        const player = gameState.players[index];
        wx.showModal({
          title: '决定顺序',
          content: `${player.name}请掷骰子`,
          showCancel: false,
          success: () => {
            const number = Math.floor(Math.random() * 6) + 1;
            playerRolls.push({ playerId: player.id, number });
            
            // 记录掷骰子日志
            this.addScoreLog(player.name, 0, `掷出${number}点`);
            
            wx.showModal({
              title: '掷骰子结果',
              content: `${player.name}掷出了${number}点`,
              showCancel: false,
              success: () => rollForOrder(index + 1)
            });
          }
        });
      };

      rollForOrder(0);
    },

    // 修改游戏结束检查条件
    checkGameOver(gameState) {
      const settings = gameState.settings || SettingsManager.getSettings();
      const winner = gameState.players.find(p => p.score >= 25000); // 修改为标准规则的获胜条件
      if (winner) {
        gameState.gameOver = true;
        gameState.winner = winner;
        return true;
      }
      return false;
    },

    // 处理骰子结果
    handleDiceRoll(e) {
      const { gameState } = this.data;
      const currentPlayer = gameState.players[gameState.currentPlayerIndex];
      
      if (currentPlayer.bankrupt) {
        wx.showToast({
          title: '该玩家已破产',
          icon: 'none'
        });
        return;
      }
      
      const { number } = e.detail;
      wx.showModal({
        title: '掷骰子',
        content: `${currentPlayer.name}掷出了${number}点`,
        showCancel: false,
        success: () => {
          // 移动玩家
          const newPosition = (currentPlayer.position + number) % this.data.squares.length;
          currentPlayer.position = newPosition;
          
          // 先更新位置
          this.updateGameState(this.data.gameState);
          
          // 检查是否经过起点
          if (newPosition < currentPlayer.position) {
            currentPlayer.score += 1000; // 经过起点奖励
            this.addScoreLog(currentPlayer.name, 1000, '经过起点');
            this.updateGameState(this.data.gameState);
          }
          
          // 获取落地格子
          const landedSquare = this.data.squares[newPosition];
          
          // 显示移动结果
          wx.showModal({
            title: '移动结果',
            content: `移动了${number}步，到达${landedSquare.name}`,
            showCancel: false,
            success: () => {
              // 处理不同类型的格子
              if (landedSquare.type === 'property') {
                this.handlePropertyLanding(landedSquare);
              } else if (landedSquare.type === 'chance') {
                this.handleChanceLanding();
              } else {
                // 如果是普通格子，询问是否结束回合
                this.confirmEndTurn(this.data.gameState, currentPlayer);
              }
            }
          });
        }
      });
    },

    // 修改确认结束回合的提示
    confirmEndTurn(gameState, player) {
      // 先检查是否游戏结束
      if (this.checkGameOver(gameState)) {
        wx.showModal({
          title: '游戏结束',
          content: `恭喜 ${gameState.winner.name} 获胜！\n成为大富翁！`,
          showCancel: false,
          success: () => {
            this.triggerEvent('gameOver', { winner: gameState.winner });
          }
        });
        return;
      }

      const nextPlayer = GameManager.nextPlayer(gameState);
      if (!nextPlayer) {
        wx.showModal({
          title: '游戏结束',
          content: '所有其他玩家已破产！',
          showCancel: false,
          success: () => {
            this.triggerEvent('gameOver', { winner: player });
          }
        });
        return;
      }

      wx.showModal({
        title: '回合操作',
        content: `当前玩家:${player.name}\n当前分数:${player.score}分\n\n\t下一回合:${nextPlayer.name}`,
        confirmText: '确定',
        showCancel: false,
        success: (res) => {
          this.updateGameState(gameState);
          this.showNextPlayerTurn(nextPlayer);
        }
      });
    },

    // 更新游戏状态的辅助方法
    updateGameState(gameState) {
      // 一次性更新所有数据
      const totalScore = gameState.players.reduce((sum, p) => sum + p.score, 0);
      const updatedPlayers = gameState.players.map(player => ({
        ...player,
        scorePercentage: totalScore > 0 ? ((player.score / totalScore) * 100).toFixed(1) : '0.0'
      }));
      
      // 再更新游戏状态
      this.setData({
        gameState: {
          ...gameState,
          players: updatedPlayers,
          totalScore,
          _updateTime: Date.now()
        }
      });
      
      // 触发一个自定义事件通知父组件更新
      this.triggerEvent('stateUpdate', { gameState });
    },

    // 修改触发玩家信息更新的方法
    triggerPlayerInfoUpdate(gameState) {
      // 直接调用 updateGameState 进行完整更新
      this.updateGameState(gameState);
    },

    // 处理落在地产格子上
    handlePropertyLanding(property) {
      let { gameState } = this.data;
      // 检查地产的所有者，而不是通过properties数组
      const owner = gameState.players.find(p => !p.bankrupt && property.ownerId === p.id);
      const currentPlayer = gameState.players[gameState.currentPlayerIndex];
      
      // 如果玩家已破产，直接结束回合
      if (currentPlayer.bankrupt) {
        this.confirmEndTurn(gameState, currentPlayer);
        return;
      }

      if (!owner) {
        wx.showModal({
          title: '购买提示',
          content: `是否购买${property.name}？\n价格：${property.price}分\n当前资金：${currentPlayer.score}分`,
          cancelText: '不购买',
          confirmText: '购买',
          success: (res) => {
            if (res.confirm) {
              const purchased = GameManager.handlePropertyPurchase(gameState, property);
              if (purchased) {
                // 更新地产的所有者颜色
                const squares = this.data.squares.map(s => {
                  if (s.id === property.id) {
                    return {
                      ...s,
                      ownerId: currentPlayer.id,
                      ownerColor: currentPlayer.color + '66'
                    };
                  }
                  return s;
                });
                
                this.updateGameState(gameState);
                this.setData({ squares });
                
                // 确保更新已经完成后再触发额外更新
                setTimeout(() => {
                  this.triggerPlayerInfoUpdate(gameState);
                }, 0);
                
                wx.showToast({
                  title: '购买成功',
                  icon: 'success',
                  duration: 1500,
                  complete: () => {
                    this.confirmEndTurn(gameState, currentPlayer);
                  }
                });
                this.addScoreLog(currentPlayer.name, -property.price, `购买了 ${property.name}`);
              } else {
                wx.showToast({
                  title: '资金不足',
                  icon: 'none',
                  complete: () => {
                    this.confirmEndTurn(gameState, currentPlayer);
                  }
                });
              }
            } else {
              this.confirmEndTurn(gameState, currentPlayer);
            }
          }
        });
      } else if (owner.id === currentPlayer.id) {
        // 如果是自己的地产，可以选择升级
        if (property.level < 3) {
          const upgradeCost = this.calculateUpgradeCost(property);
          wx.showModal({
            title: '升级提示',
            content: `是否升级${property.name}？\n升级费用：${upgradeCost.cost}分\n当前资金：${currentPlayer.score}分\n升级后过路费：${this.calculateTollFee(property, property.level + 1)}分`,
            cancelText: '不升级',
            confirmText: '升级',
            success: (res) => {
              if (res.confirm && currentPlayer.score >= upgradeCost.cost) {
                currentPlayer.score -= upgradeCost.cost;
                property.price = upgradeCost.newPrice;
                property.level += 1;
                this.updateGameState(gameState);
                this.addScoreLog(currentPlayer.name, -upgradeCost.cost, `升级 ${property.name} 到 ${property.level} 级`);
              }
              this.confirmEndTurn(gameState, currentPlayer);
            }
          });
        } else {
          wx.showToast({
            title: '已达到最高等级',
            icon: 'none'
          });
          this.confirmEndTurn(gameState, currentPlayer);
        }
      } else {
        // 需要支付过路费
        const tollFee = this.calculateTollFee(property, property.level);
        wx.showModal({
          title: '支付过路费',
          content: `需要支付过路费${tollFee}分给${owner.name}\n(${property.name} ${property.level}级)`,
          showCancel: false,
          success: () => {
            if (currentPlayer.score >= tollFee) {
              currentPlayer.score -= tollFee;
              owner.score += tollFee;
              this.updateGameState(gameState);
              this.addScoreLog(currentPlayer.name, -tollFee, `支付过路费给 ${owner.name}`);
              this.addScoreLog(owner.name, tollFee, `收取 ${currentPlayer.name} 过路费`);
              this.confirmEndTurn(gameState, currentPlayer);
            } else {
              this.handleInsufficientFunds(currentPlayer, owner, tollFee, property);
            }
          }
        });
      }
    },

    // 计算升级费用
    calculateUpgradeCost(property) {
      if (property.level === 1) {
        const cost = Math.floor(property.price * 0.3);
        return {
          cost,
          newPrice: property.price + cost
        };
      } else if (property.level === 2) {
        const cost = Math.floor(property.price * 0.5);
        return {
          cost,
          newPrice: property.price + cost
        };
      }
      return { cost: 0, newPrice: property.price };
    },

    // 计算过路费
    calculateTollFee(property, level) {
      switch(level) {
        case 1: return Math.floor(property.price * 0.2);  // 基础过路费为地产价值的20%
        case 2: return Math.floor(property.price * 0.4);  // 2级地产过路费为地产价值的40%
        case 3: return Math.floor(property.price * 0.6);  // 3级地产过路费为地产价值的60%
        default: return 500;
      }
    },

    // 处理资金不足
    handleInsufficientFunds(player, owner, tollFee, property) {
      // 计算玩家所有资产
      const totalAssets = player.score + this.calculateTotalPropertyValue(player);
      
      // 如果总资产不足以支付，直接破产
      if (totalAssets < tollFee) {
        this.handleBankruptcy(player);
        return;
      }
      
      const ownedProperties = this.data.squares.filter(s => 
        s.type === 'property' && player.properties.includes(s.id)
      );
      
      if (ownedProperties.length > 0) {
        wx.showModal({
          title: '资金不足',
          content: `需要支付${tollFee}分\n当前资金：${player.score}分\n需要出售地产来支付过路费`,
          success: (res) => {
            if (res.confirm) {
              this.showSellPropertyDialog(player, owner, tollFee, property);
            } else {
              this.handleBankruptcy(player);
            }
          }
        });
      } else {
        this.handleBankruptcy(player);
      }
    },

    // 计算玩家地产总价值
    calculateTotalPropertyValue(player) {
      return this.data.squares
        .filter(s => s.type === 'property' && player.properties.includes(s.id))
        .reduce((sum, property) => sum + property.price, 0);
    },

    // 显示出售地产对话框
    showSellPropertyDialog(player, owner, amount, property, reason = '') {
      const ownedProperties = this.data.squares.filter(s => 
        s.type === 'property' && player.properties.includes(s.id)
      );
      
      if (ownedProperties.length === 0) {
        // 如果没有可出售的地产，直接破产
        this.handleBankruptcy(player);
        return;
      }
      
      wx.showActionSheet({
        itemList: ownedProperties.map(p => `${p.name} (${p.price}分)`),
        success: (res) => {
          const selectedProperty = ownedProperties[res.tapIndex];
          this.sellProperty(player, selectedProperty);
          
          // 检查是否筹够了足够的资金
          if (player.score >= amount) {
            if (owner) {
              // 如果是支付过路费
              player.score -= amount;
              owner.score += amount;
              this.updateGameState(this.data.gameState);
              this.addScoreLog(player.name, -amount, `支付过路费给 ${owner.name}`);
              this.addScoreLog(owner.name, amount, `收取 ${player.name} 过路费`);
            } else {
              // 如果是机会命运事件
              player.score -= amount;
              this.updateGameState(this.data.gameState);
              this.addScoreLog(player.name, -amount, reason || '支付费用');
            }
            this.confirmEndTurn(this.data.gameState, player);
          } else {
            // 如果还是不够，继续显示出售对话框
            this.showSellPropertyDialog(player, owner, amount, property, reason);
          }
        },
        fail: () => {
          // 如果玩家取消选择，则破产
          this.handleBankruptcy(player);
        }
      });
    },

    // 出售地产
    sellProperty(player, property) {
      player.score += property.price;
      player.properties = player.properties.filter(id => id !== property.id);
      
      // 更新地产显示
      const squares = this.data.squares.map(s => {
        if (s.id === property.id) {
          return {
            ...s,
            ownerId: null,
            ownerColor: '#fff',
            level: 1
          };
        }
        return s;
      });
      
      property.ownerId = null;
      property.level = 1;
      this.setData({ squares });
      
      this.addScoreLog(player.name, property.price, `出售 ${property.name}`);
    },

    // 处理破产
    handleBankruptcy(player) {
      const updates = {};
      
      // 记录破产前的分数
      const previousScore = player.score;
      
      // 批量处理地产更新
      this.data.squares.forEach((square, index) => {
        if (square.type === 'property' && player.properties.includes(square.id)) {
          updates[`squares[${index}].ownerId`] = null;
          updates[`squares[${index}].ownerColor`] = '#fff';
          updates[`squares[${index}].level`] = 1;
          // 记录每个被清空的地产
          this.addScoreLog(player.name, -square.price, `失去地产 ${square.name}`);
        }
      });
      
      player.properties = [];
      player.score = 0;
      player.bankrupt = true;
      
      // 一次性更新所有数据
      this.setData(updates);
      this.updateGameState(this.data.gameState);
      
      this.addScoreLog(player.name, -previousScore, '破产');
      
      // 检查是否只剩一个未破产的玩家
      const activePlayers = this.data.gameState.players.filter(p => !p.bankrupt);
      if (activePlayers.length === 1 || this.shouldEndGame()) {
        // 游戏结束，找出得分最高的未破产玩家作为获胜者
        const winner = activePlayers.reduce((prev, curr) => 
          prev.score > curr.score ? prev : curr
        );
        this.data.gameState.gameOver = true;
        this.data.gameState.winner = winner;
        this.updateGameState(this.data.gameState);
        
        wx.showModal({
          title: '游戏结束',
          content: `${winner.name} 获得胜利！\n最终得分：${winner.score}分`,
          showCancel: false,
          success: () => {
            this.triggerEvent('gameOver', { winner });
          }
        });
        return;
      }
      
      wx.showModal({
        title: '破产',
        content: `${player.name}已破产！`,
        showCancel: false,
        success: () => {
          this.confirmEndTurn(this.data.gameState, player);
        }
      });
    },

    // 判断是否应该结束游戏
    shouldEndGame() {
      const { gameState } = this.data;
      const activePlayers = gameState.players.filter(p => !p.bankrupt);
      // 如果只剩一个玩家未破产，或者有玩家达到胜利分数，游戏结束
      return activePlayers.length === 1 || activePlayers.some(p => p.score >= gameState.settings.winScore);
    },

    // 处理落在机会格子上
    handleChanceLanding() {
      const event = GameManager.handleChanceEvent(this.data.gameState);
      
      // 先更新游戏状态
      this.updateGameState(this.data.gameState);
      
      if (event.type === 'needSell') {
        // 显示出售地产对话框
        this.showSellPropertyDialog(
          this.data.gameState.players[this.data.gameState.currentPlayerIndex],
          null,  // 没有接收者
          event.amount,  // 需要筹集的金额
          null,  // 没有相关地产
          event.desc  // 事件描述
        );
        return;
      }
      
      // 显示事件结果
      wx.showModal({
        title: '机会命运',
        content: `${event.desc}\n分数${event.amount > 0 ? '增加' : '减少'}了 ${Math.abs(event.amount)} 分`,
        showCancel: false,
        success: () => {
          // 确认是否结束回合
          this.confirmEndTurn(this.data.gameState, this.data.gameState.players[this.data.gameState.currentPlayerIndex]);
        }
      });
    },

    handleSquareTouchStart(e) {
      const id = e.currentTarget.dataset.id;
      const squares = this.data.squares.map(square => ({
        ...square,
        active: square.id === id
      }));
      this.setData({ squares });
    },

    handleSquareTouchEnd() {
      const squares = this.data.squares.map(square => ({
        ...square,
        active: false
      }));
      this.setData({ squares });
    },

    showNextPlayerTurn(player) {
      // 更新当前玩家索引和状态
      const currentIndex = this.data.gameState.players.findIndex(p => p.id === player.id);
      this.setData({
        'gameState.currentPlayerIndex': currentIndex,
        'gameState._updateTime': Date.now()  // 强制触发更新
      });
      
      // 确保玩家信息更新
      this.triggerPlayerInfoUpdate(this.data.gameState);
      
      wx.showModal({
        title: '回合提示',
        content: `轮到 ${player.name} 的回合\n当前分数：${player.score}分\n\n请掷骰子进行移动`,
        showCancel: false,
        confirmText: '确定'
      });
    },

    // 修改分数记录方法
    addScoreLog(playerName, amount, desc) {
      const now = new Date();
      const time = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`;
      // 如果金额为0，不添加+/-符号
      const formattedAmount = amount === 0 ? 0 : amount;
      const log = {
        timestamp: now.getTime(),
        time,
        playerName,
        amount: formattedAmount,
        type: amount > 0 ? 'increase' : amount < 0 ? 'decrease' : 'neutral',
        desc
      };
      
      // 直接更新分数记录
      this.setData({
        scoreLogs: [log, ...this.data.scoreLogs].slice(0, 50)
      });
    },

    handlePropertyPurchase(property, currentPlayer) {
      // 检查玩家是否有足够的资金
      if (currentPlayer.score < property.price) {
        return false;
      }
      
      // 扣除玩家资金
      currentPlayer.score -= property.price;
      currentPlayer.properties.push(property.id);
      
      // 批量更新数据
      const updates = {
        [`squares[${property.id}].ownerId`]: currentPlayer.id,
        [`squares[${property.id}].ownerColor`]: currentPlayer.color + '66',
        [`squares[${property.id}].level`]: 1
      };
      
      this.setData(updates);
      return true;
    },

    // 添加防抖方法
    debounceUpdate(func, wait = 100) {
      if (this.data.updateTimer) {
        clearTimeout(this.data.updateTimer);
      }
      const timer = setTimeout(() => {
        func();
      }, wait);
      this.setData({ updateTimer: timer });
    }
  }
}); 