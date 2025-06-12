import { SettingsManager } from '../../utils/settingsManager';

Page({
  data: {
    settings: null
  },

  onLoad() {
    this.setData({
      settings: SettingsManager.getSettings()
    });
  },

  // 设置变更处理函数
  onInitialScoreChange(e) {
    this.updateSettings('initialScore', e.detail.value);
  },

  onPassingStartBonusChange(e) {
    this.updateSettings('passingStartBonus', e.detail.value);
  },

  onTollFeeChange(e) {
    this.updateSettings('tollFee', e.detail.value);
  },

  onWinScoreChange(e) {
    this.updateSettings('winScore', e.detail.value);
  },

  onPlayerCountChange(e) {
    this.updateSettings('playerCount', Number(e.detail.value) + 2);
  },

  onSoundChange(e) {
    this.updateSettings('soundEnabled', e.detail.value);
  },

  onAnimationChange(e) {
    this.updateSettings('animationEnabled', e.detail.value);
  },

  onChanceProbabilityChange(e) {
    const { event } = e.currentTarget.dataset;
    const value = e.detail.value;
    
    this.setData({
      ['settings.chanceEventProbability.' + event]: value
    });
  },

  // 更新设置
  updateSettings(key, value) {
    this.setData({
      ['settings.' + key]: value
    });
  },

  // 重置设置
  resetSettings() {
    wx.showModal({
      title: '确认重置',
      content: '是否要将所有设置恢复为默认值？',
      success: (res) => {
        if (res.confirm) {
          SettingsManager.resetSettings();
          this.setData({
            settings: SettingsManager.getSettings()
          });
          wx.showToast({
            title: '设置已重置',
            icon: 'success'
          });
        }
      }
    });
  },

  // 保存设置
  saveSettings() {
    if (SettingsManager.saveSettings(this.data.settings)) {
      wx.showToast({
        title: '设置已保存',
        icon: 'success'
      });
      
      // 返回上一页
      wx.navigateBack();
    } else {
      wx.showToast({
        title: '保存失败',
        icon: 'error'
      });
    }
  }
}); 