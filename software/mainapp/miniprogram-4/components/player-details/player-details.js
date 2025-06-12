Component({
  properties: {
    player: {
      type: Object,
      observer(newVal, oldVal) {
        if (newVal && JSON.stringify(newVal) !== JSON.stringify(this.data.playerData)) {
          this.setData({
            playerData: JSON.parse(JSON.stringify(newVal))
          });
        }
      }
    }
  },

  data: {
    playerData: null
  },

  observers: {
    'playerData': function(playerData) {
      if (playerData) {
        // 强制更新视图
        this.setData({
          playerData: { ...playerData, _forceUpdate: Date.now() }
        });
      }
    }
  },

  lifetimes: {
    attached() {
      if (this.properties.player) {
        this.setData({
          playerData: JSON.parse(JSON.stringify(this.properties.player))
        });
      }
    }
  }
}); 