import { SettingsManager } from './settingsManager';

export const GameManager = {
  // 初始化游戏状态
  initGameState() {
    const settings = SettingsManager.getSettings();
    // 初始化棋盘格子
    const squares = [
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
    ];

    return {
      players: [
        { id: 1, name: '玩家1', score: 3500, position: 0, properties: [], color: '#FF5252' },
        { id: 2, name: '玩家2', score: 3500, position: 0, properties: [], color: '#4CAF50' },
        { id: 3, name: '玩家3', score: 3500, position: 0, properties: [], color: '#2196F3' },
        { id: 4, name: '玩家4', score: 3500, position: 0, properties: [], color: '#FFC107' }
      ],
      currentPlayerIndex: 0,
      currentPlayerMoved: false,
      gameOver: false,
      winner: null,
      settings: settings,
      squares: squares
    };
  },

  // 处理玩家移动
  handlePlayerMove(gameState, steps) {
    if (!gameState || !gameState.settings) {
      console.error('游戏状态或设置未初始化');
      return null;
    }
    if (gameState.currentPlayerMoved) {
      console.warn('当前玩家已经行动过');
      return null;
    }

    const settings = gameState.settings || SettingsManager.getSettings();
    const player = gameState.players[gameState.currentPlayerIndex];
    const oldPosition = player.position;
    const boardSize = 40;
    
    const newPosition = (oldPosition + steps) % boardSize;
    
    // 检查是否经过起点（但不是刚好停在起点上）
    if (newPosition < oldPosition && newPosition !== 0) {
      player.score += settings.passingStartBonus;
      this.updateTotalScore(gameState);
    }
    
    player.position = newPosition;
    gameState.currentPlayerMoved = true;
    return player;
  },

  // 处理购买地产
  handlePropertyPurchase(gameState, property) {
    const player = gameState.players[gameState.currentPlayerIndex];
    
    if (player.score >= property.price) {
      player.score -= property.price;
      player.properties.push(property.id);
      property.ownerId = player.id;  // 设置地产所有者ID
      property.level = 1;  // 初始化地产等级
      // 更新总分数
      this.updateTotalScore(gameState);
      return true;
    }
    return false;
  },

  // 处理支付过路费
  handleTollPayment(gameState, propertyId) {
    const settings = gameState.settings || SettingsManager.getSettings();
    const currentPlayer = gameState.players[gameState.currentPlayerIndex];
    const owner = gameState.players.find(p => p.properties.includes(propertyId));
    
    if (owner && currentPlayer.score >= settings.tollFee) {
      currentPlayer.score -= settings.tollFee;
      owner.score += settings.tollFee;
      // 更新总分数
      this.updateTotalScore(gameState);
      return true;
    } else if (owner) {
      this.handleBankruptcy(gameState, currentPlayer.id);
      return false;
    }
    return true;
  },

  // 处理机会命运事件
  handleChanceEvent(gameState) {
    const settings = gameState.settings || SettingsManager.getSettings();
    const player = gameState.players[gameState.currentPlayerIndex];
    
    // 根据概率生成事件
    const events = [
      { type: 'add', amount: 1000, desc: '股票上涨', prob: settings.chanceEventProbability.bonus1000 },
      { type: 'add', amount: 3000, desc: '中了彩票', prob: settings.chanceEventProbability.bonus3000 },
      { type: 'subtract', amount: -1000, desc: '医疗支出', prob: settings.chanceEventProbability.penalty1000 },
      { type: 'subtract', amount: -2500, desc: '投资失败', prob: settings.chanceEventProbability.penalty2500 }
    ];
    
    // 计算总概率
    const totalProb = events.reduce((sum, event) => sum + event.prob, 0);
    let random = Math.random() * totalProb;
    
    // 选择事件
    let selectedEvent = events[events.length - 1];
    for (const event of events) {
      if (random < event.prob) {
        selectedEvent = event;
        break;
      }
      random -= event.prob;
    }
    
    // 如果是扣分事件，先检查玩家是否会破产
    if (selectedEvent.type === 'subtract') {
      // 计算玩家总资产（现金 + 地产价值）
      const propertyValue = player.properties.reduce((sum, propId) => {
        const property = gameState.squares?.find(s => s.id === propId);
        return sum + (property ? property.price : 0);
      }, 0);
      const totalAssets = player.score + propertyValue;
      
      // 如果扣分后总资产为负，则玩家破产
      if (totalAssets < Math.abs(selectedEvent.amount)) {
        this.handleBankruptcy(gameState, player.id);
        return {
          ...selectedEvent,
          amount: -player.score,
          desc: selectedEvent.desc + '（破产）'
        };
      }
    }
    
    if (selectedEvent.type === 'add') {
      player.score += selectedEvent.amount;
    } else {
      // 如果玩家现金不足，需要出售地产
      if (player.score < Math.abs(selectedEvent.amount)) {
        // 提示玩家选择要出售的地产
        return {
          type: 'needSell',
          amount: Math.abs(selectedEvent.amount),
          desc: selectedEvent.desc
        };
      }
      player.score += selectedEvent.amount;
    }
    
    // 更新总分数
    this.updateTotalScore(gameState);
    
    return {
      ...selectedEvent,
      amount: selectedEvent.amount
    };
  },

  // 处理破产
  handleBankruptcy(gameState, playerId) {
    const player = gameState.players.find(p => p.id === playerId);
    if (!player) return;

    // 记录破产前的资产
    const previousAssets = {
      score: player.score,
      properties: [...player.properties]
    };
    
    // 清空玩家资产
    player.score = 0;
    player.properties = [];
    player.bankrupt = true;
    
    // 归还所有地产
    gameState.squares.forEach(square => {
      if (square.type === 'property' && square.ownerId === playerId) {
        square.ownerId = null;
        square.level = 1;
        square.ownerColor = '#fff';
      }
    });
    
    // 更新总分数
    this.updateTotalScore(gameState);
    
    // 检查游戏是否应该结束
    const activePlayers = gameState.players.filter(p => !p.bankrupt);
    if (activePlayers.length === 1) {
      gameState.gameOver = true;
      gameState.winner = activePlayers[0];
    }
    
    return {
      playerId,
      previousAssets
    };
  },

  // 新增：更新总分数
  updateTotalScore(gameState) {
    if (!gameState || !gameState.players) {
      console.error('游戏状态未初始化');
      return;
    }
    // 计算所有玩家的总分数
    const totalScore = gameState.players.reduce((sum, player) => sum + player.score, 0);
    gameState.totalScore = totalScore;
    
    // 更新每个玩家的分数占比
    gameState.players.forEach(player => {
      player.scorePercentage = (player.score / totalScore * 100).toFixed(1);
    });
  },

  // 检查游戏是否结束
  checkGameOver(gameState) {
    const settings = gameState.settings || SettingsManager.getSettings();
    const winner = gameState.players.find(p => p.score >= settings.winScore);
    if (winner) {
      gameState.gameOver = true;
      gameState.winner = winner;
      // 最后更新一次总分数
      this.updateTotalScore(gameState);
      return true;
    }
    return false;
  },

  // 切换到下一个玩家
  nextPlayer(gameState) {
    gameState.currentPlayerMoved = false;
    
    let nextIndex = gameState.currentPlayerIndex;
    do {
      nextIndex = (nextIndex + 1) % gameState.players.length;
    } while (gameState.players[nextIndex].bankrupt && nextIndex !== gameState.currentPlayerIndex);
    
    if (nextIndex === gameState.currentPlayerIndex && gameState.players[nextIndex].bankrupt) {
      gameState.gameOver = true;
      return null;
    }
    
    gameState.currentPlayerIndex = nextIndex;
    return gameState.players[nextIndex];
  }
}; 