Component({
  properties: {
    player: {
      type: Object,
    },
    isCurrentPlayer: {
      type: Boolean,
      value: false
    }
  },

  data: {
    playerData: null
  },

  lifetimes: {
    attached() {
      this.setData({ 
        playerData: {
          ...this.properties.player,
          properties: [...this.properties.player.properties]
        }
      });
    }
  },

  observers: {
    'player.**': function(player) {
      // 深度监听 player 对象的所有属性变化
      if (player) {
        this.setData({
          playerData: {
            ...player,
            properties: [...player.properties]
          }
        });
      }
    }
  },

  methods: {
    // 显示分数增加动画
    showScoreIncrease() {
      this.setData({
        showScoreAnimation: true,
        scoreChangeAmount: this.data.player.score - this.data.lastScore
      });
      setTimeout(() => {
        this.setData({ showScoreAnimation: false });
      }, 1000);
    },

    // 显示分数减少动画
    showScoreDecrease() {
      this.setData({
        showScoreAnimation: true,
        scoreChangeAmount: this.data.player.score - this.data.lastScore
      });
      setTimeout(() => {
        this.setData({ showScoreAnimation: false });
      }, 1000);
    }
  }
}); 