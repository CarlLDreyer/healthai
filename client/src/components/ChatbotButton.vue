<template>
  <div class="chatbot-icon-wrapper" @click="handleClick">
    <div class="chatbot-icon">
      <transition name="rotate" mode="out-in">
        <svg viewBox="0 0 24 24" :class="{'close': chatOpen}" :key="!chatOpen"><use :xlink:href="selectedIcon" /></svg>
      </transition>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ChatbotButton',
  methods: {
    ...mapActions([
      'setChatOpen'
    ]),
    handleClick () {
      this.setChatOpen(!this.chatOpen)
    }
  },
  computed: {
    ...mapGetters([
      'chatOpen'
    ]),
    selectedIcon () {
      return this.chatOpen ? '#close' : '#bubbles'
    }
  },
}
</script>

<style lang="scss" scoped>
.chatbot-icon-wrapper {
  position: absolute;
  background: rgba(126, 87, 194, 0.25);
  height: 80px;
  width: 80px;
  border-radius: 50%;
  bottom: 32px;
  right: 32px;
  cursor: pointer;
  .chatbot-icon {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #7E57C2;
    height: 64px;
    width: 64px;
    border-radius: 50%;
    margin: 8px 0 0 8px;
    svg {
      height: 32px;
      width: 32px;
      fill: none;
      stroke: white;
      stroke-width: 1.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      position: absolute;
      &.close {
        height: 44px;
        width: 44px;
      }
    }
  }
}
.rotate-enter-active, .rotate-leave-active {
  transition: all .1s ease;
}
.rotate-enter, .rotate-leave-to {
  opacity: 0;
  transform: scale(0.5);
}
</style>
