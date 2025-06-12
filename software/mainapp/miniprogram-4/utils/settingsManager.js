export const SettingsManager = {
  // 默认设置
  defaultSettings: {
    initialScore: 3500,
    passingStartBonus: 1000,
    tollFee: 500,
    winScore: 25000,
    playerCount: 4,
    soundEnabled: true,
    animationEnabled: true,
    // 自定义机会命运卡片概率
    chanceEventProbability: {
      bonus1000: 25,
      bonus3000: 15,
      penalty1000: 35,
      penalty2500: 25
    }
  },

  // 获取设置
  getSettings() {
    try {
      const settings = wx.getStorageSync('gameSettings');
      return settings ? JSON.parse(settings) : this.defaultSettings;
    } catch (e) {
      console.error('读取设置失败:', e);
      return this.defaultSettings;
    }
  },

  // 保存设置
  saveSettings(settings) {
    try {
      wx.setStorageSync('gameSettings', JSON.stringify(settings));
      return true;
    } catch (e) {
      console.error('保存设置失败:', e);
      return false;
    }
  },

  // 重置设置
  resetSettings() {
    return this.saveSettings(this.defaultSettings);
  }
}; 