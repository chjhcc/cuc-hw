// index.js
Page({
  data: {
    gameStarted: false
  },

  startGame() {
    setTimeout(() => {
      wx.navigateTo({
        url: '/pages/game/game',
        success: () => {
          console.log('成功跳转到游戏页面');
        },
        fail: (error) => {
          console.error('跳转失败:', error);
          wx.showToast({
            title: '启动游戏失败',
            icon: 'none'
          });
        }
      });
    }, 100);
  },

  goToSettings() {
    setTimeout(() => {
      wx.navigateTo({
        url: '/pages/settings/settings',
        success: () => {
          console.log('成功跳转到设置页面');
        },
        fail: (error) => {
          console.error('跳转失败:', error);
          wx.showToast({
            title: '打开设置失败',
            icon: 'none'
          });
        }
      });
    }, 100);
  }
});
