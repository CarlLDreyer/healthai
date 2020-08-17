<template>
  <section>
    <h1>Health.ai</h1>
    <Chatbot />
  </section>
</template>

<script>
import Chatbot from '@/components/Chatbot'
export default {
  name: 'Home',
  components: {
    Chatbot
  }
}
</script>

<style lang="scss" scoped>
section {
  background: #242424;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
h1 {
  color: white;
  letter-spacing: 0.5px;
  font-size: 48px;
  user-select: none;
}
</style>
