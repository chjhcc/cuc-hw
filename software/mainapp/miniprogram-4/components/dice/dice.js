Component({
  properties: {
    disabled: {
      type: Boolean,
      value: false
    }
  },

  data: {
    diceNumber: 1,
    animating: false,
    shakeAnimation: false,
    rotateX: 0,
    rotateY: 0
  },

  methods: {
    roll() {
      if (this.data.animating || this.properties.disabled) return;
      
      this.setData({ 
        animating: true,
        shakeAnimation: true
      });
      
      // 骰子动画
      let count = 0;
      const rollInterval = setInterval(() => {
        // 3D 旋转动画
        this.setData({
          diceNumber: Math.floor(Math.random() * 6) + 1,
          rotateY: Math.random() * 360,
          rotateX: Math.random() * 360
        });
        
        count++;
        if (count > 10) {
          clearInterval(rollInterval);
          const finalNumber = Math.floor(Math.random() * 6) + 1;
          
          this.setData({ 
            diceNumber: finalNumber,
            animating: false,
            shakeAnimation: false,
            rotateX: 0,
            rotateY: 0
          });
          
          // 通知父组件骰子点数
          this.triggerEvent('rolled', { number: finalNumber });
        }
      }, 100);
    },

    // 设置骰子点数（用于外部控制）
    setNumber(number) {
      this.setData({ diceNumber: number });
    }
  }
}); 