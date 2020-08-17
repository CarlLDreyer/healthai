<template>
<!-- FIX THE ANIMATION -->
  <div class="typing-indicator">
    <span class="avatar bot">
      <!-- <svg viewBox="0 0 32 32"><use xlink:href="#robot" /></svg> -->
    </span>
    <div class="dots">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TypingIndicator'
}
</script>

<style lang="scss" scoped>
.typing-indicator {
  display: flex;
  position: relative;
  justify-content: flex-start;
  margin-bottom: 8px;
  .avatar {
    line-height: 32px;
    text-align: center;
    // margin: 5px 8px 5px 0;
    margin: -8px 8px 0 0;
    display: block;
    height: 36px;
    width: 36px;
    border-radius: 50%;
    background: url('../assets/Avatar.png');
    background-size: cover;
    background-position: center;
  }
  .dots {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #EADDFF;
    padding: 12px 16px;
    height: 42px;
    box-sizing: border-box;
    border-radius: 4px 14px 14px 14px;
    span {
      display: inline-block;
      background-color: #747474;
      width: 6px;
      height: 6px;
      border-radius: 100%;
      animation: bob 1.5s infinite;
      &:nth-child(1) {
        animation-delay: -0.2s;
      }
      &:nth-child(2) {
        animation-delay: -0.1s;
        margin: 0 4px;
      }
      &:nth-child(3) {
        animation-delay: 0s;
      }
    }
  }
}

@keyframes bob {
  10% {
    transform: translateY(-6px);
    background-color: #9E9DA2;
  }
  50% {
    transform: translateY(0);
    background-color: #B6B5BA;
  }
}
</style>
