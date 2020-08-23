<template>
  <section>
    <h1>{{ health }}</h1>
    <p>{{ desc }}</p>
    <Chatbot />
  </section>
</template>

<script>
import Chatbot from '@/components/Chatbot'
export default {
  name: 'Home',
  components: {
    Chatbot
  },
  data () {
    return {
      health: 'Health.ai',
      desc: 'An AI-driven medical assistant'
    }
  },
}
</script>

<style lang="scss" scoped>
section {
  background: #242424;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
    h1 {
      letter-spacing: 0.5px;
      margin-bottom: 0;
      font-size: 48px;
    }
    p {
      margin-top: 0;
      font-size: 18px;
    }
}
</style>
