// pages/game/game.js
import { GameManager } from '../../utils/gameManager';

Page({
  data: {
    gameState: null,
    isReady: false
  },

  onLoad() {
    setTimeout(() => {
      this.initGame();
      this.setData({ isReady: true });
    }, 300);
  },

  initGame() {
    const gameState = GameManager.initGameState();
    this.setData({ gameState });
  },

  handleDiceRoll(e) {
    if (!this.data.isReady) {
      wx.showToast({
        title: '游戏正在准备中',
        icon: 'none'
      });
      return;
    }

    const gameBoard = this.selectComponent('#gameBoard');
    if (gameBoard) {
      gameBoard.handleDiceRoll(e);
    }
  },

  handleGameOver(e) {
    if (!this.data.isReady) return;

    const { winner } = e.detail;
    wx.nextTick(() => {
      wx.navigateTo({
        url: `/pages/result/result?winner=${JSON.stringify(winner)}`,
        success: () => {
          console.log('成功跳转到结果页面');
        },
        fail: (error) => {
          console.error('跳转失败:', error);
          wx.showToast({
            title: '无法显示结果',
            icon: 'none'
          });
        }
      });
    });
  },

  onGameStateUpdate(event) {
    if (!this.data.isReady) return;

    const { gameState } = event.detail;
    wx.nextTick(() => {
      this.setData({
        gameState: JSON.parse(JSON.stringify(gameState))
      });
    });
  },

  onUnload() {
    this.setData({
      gameState: null,
      isReady: false
    });
  }
});