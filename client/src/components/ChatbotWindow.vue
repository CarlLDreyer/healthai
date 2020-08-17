<template>
  <transition name="fade-zoom">
    <div class="chatbot-window" v-if="chatOpen">
      <div class="header">
        <span class="avatar"></span>
        <span class="text">
          <span class="name">Jullan</span>
          <span class="status">Active now</span>
        </span>
        <span class="mobile-close" @click="setChatOpen(false)">
          <svg viewBox="0 0 24 24"><use xlink:href="#close" /></svg>
        </span>
      </div>
      <div class="message-body" id="chatWindow" :class="{'short': hasButtons}">
        <TypingIndicator v-show="isTyping" />
        <ChatbotMsg v-for="message in messages" :key="message.id" :message="message" :class="setMessageBorder(message)" />
      </div>
      <div class="message-buttons" v-if="hasButtons">
        <Button v-for="button in buttons" :key="button.id" @click="handleButtonClick(button)">{{ button.title }}</Button>
      </div>
      <div class="message-input">
        <input :value="userInput"
                  @input="userInput = $event.target.value"
                  @keydown.enter.prevent="handleUserQuestion"
                  placeholder="Ask me anything..."
                  ref="inputArea"
        >
        </input>
        <button @click="handleUserQuestion">
          <svg viewBox="0 0 448 512"><use xlink:href="#send" /></svg>
        </button>
      </div>
    </div>
  </transition>
</template>

<script>
import rasaApi from '@/utils/rasaApi'
import Message from '@/utils/Message'
import ChatbotMsg from '@/components/ChatbotMsg'
import TypingIndicator from '@/components/TypingIndicator'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ChatbotWindow',
  data () {
    return {
      Message,
      messages: [],
      messageQueue: [],
      userInput: '',
      isTyping: false,
      initialShown: false,
      buttons: [],
    }
  },
  components: {
    ChatbotMsg,
    TypingIndicator,
  },
  methods: {
    ...mapActions([
      'setChatOpen'
    ]),
    welcomeMessages () {
      let firstMessage = { sender: 'bot', text: 'Hey! 👋' }
      let secondMessage = { sender: 'bot', text: 'My name\'s Jullan and I\'m a virtual health care assistant. 🤖' }
      let thirdMessage = { sender: 'bot', text: 'You can ask me questions about various diseases and medicines. 💊' }
      this.addToMessageQueue(firstMessage)
      this.addToMessageQueue(secondMessage)
      this.addToMessageQueue(thirdMessage)
    },
    createNewMessage (message) {
      let { text, sender, list, link, buttons } = message
      this.messages.unshift({ text: text, sender: sender, ...(list && { list }), ...(link && { link }), ...(buttons && { buttons }) })
    },
    addToMessageQueue (message) {
      this.messageQueue.push(message)
    },
    async handleBotResponse (message) {
      let query = { text: message, sender: 'user' }
      const response = await rasaApi.talkToBot(query)
      let { data } = response
      let parsedData = this.parseResponse(data)
      for (let o in parsedData) {
        this.addToMessageQueue(parsedData[o])
      }
    },
    handleUserQuestion () {
      if (!this.userInput.trim().length) return
      let message = { sender: 'user', text: this.userInput }
      this.createNewMessage(message)
      this.handleBotResponse(message.text)
      this.userInput = ''
    },
    parseResponse (data) {
      let response = []
      let length = data.length
      for (let i = 0; i < length; i += 2) {
        let recipient = data[i].recipient_id
        let text = data[i]?.text
        let list = data[i + 1]?.attachment?.symptoms
        let link = data[i + 1]?.attachment?.link
        let buttons = data[i + 1]?.attachment?.buttons
        if (link) response.push({ sender: 'bot', recipient, ...(text && { text }), ...(list && { list }) }, { sender: 'bot', recipient, link, ...(buttons && { buttons }) })
        else response.push({ sender: 'bot', recipient, ...(text && { text }), ...(list && { list }), ...(buttons && { buttons }) })
      }
      return response
    },
    setMessageBorder (message) {
      let { sender } = message
      let messageIndex = this.messages.indexOf(message)
      let previous = this.messages[messageIndex + 1] || {}
      let next = this.messages[messageIndex - 1] || {}
      if (previous.sender !== sender && next.sender === sender) return 'first'
      else if (previous.sender === sender && next.sender !== sender) return 'last'
      else if (previous.sender === sender && next.sender === sender) return 'middle'
      else return ''
    },
    handleButtonClick (button) {
      let { payload, title } = button || ''
      let message = { sender: 'user', text: title }
      this.createNewMessage(message)
      this.handleBotResponse(payload)
    },
  },
  watch: {
    messages (message) {
      this.$nextTick(() => {
        let chat = document.getElementById('chatWindow') || {}
        chat.scrollTop = chat.scrollHeight
      })
      if (message[0]?.hasOwnProperty('buttons')) {
        let { buttons } = message[0] || []
        this.buttons = buttons
      }
      else if (this.buttons !== []) {
        this.buttons = []
      }
    },
    messageQueue (queue) {
      let test = queue[0] || {}
      if (Object.keys(test).length === 0 && test.constructor === Object) return
      this.isTyping = true
      const delay = ((queue[0]?.text?.length / 50) * 1000) || 80
      let calculatedTime = delay > 2000 ? 2000 : delay < 500 ? 750 : delay
      setTimeout(() => {
        this.isTyping = false
        return new Promise((resolve) => {
          let message = queue.shift()
          if (message !== undefined) this.createNewMessage(message)
          setTimeout(resolve, 1500)
        })
      }, calculatedTime)
    },
    chatOpen (isOpen) {
      if (!this.initialShown) {
        this.welcomeMessages()
        this.initialShown = true
      }
    },
  },
  computed: {
    ...mapGetters({
      chatOpen: 'chatOpen'
    }),
    hasInput () {
      return this.userInput.length > 0
    },
    hasButtons () {
      return this.buttons.length > 0
    },
  },
}
</script>

<style lang="scss" scoped>
.chatbot-window {
  position: absolute;
  width: 360px;
  border-radius: 10px;
  overflow: hidden;
  right: 32px;
  bottom: 132px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  @media (max-width: 764px) {
    width: 100%;
    right: 0;
    bottom: 0;
  }
  .header {
    background: #7E57C2;
    display: flex;
    align-items: center;
    .avatar {
      display: block;
      height: 48px;
      width: 48px;
      border-radius: 50%;
      background: url('../assets/Avatar.png');
      background-size: cover;
      background-position: center;
      margin: 12px 16px;
    }
    .text {
      color: white;
      display: flex;
      flex: 1;
      flex-direction: column;
      text-align: left;
      .name {
        font-size: 18px;
      }
      .status {
        font-size: 12px;
        font-weight: 300;
        opacity: 0.75;
      }
    }
    .mobile-close {
      @media (max-width: 764px) {
        cursor: pointer;
        margin-right: 8px;
        svg {
          width: 38px;
          height: 38px;
          fill: none;
          stroke: white;
          stroke-linecap: round;
          stroke-linecap: round;
          vertical-align: sub;
        }
      }
    }
  }
  .message-body {
    max-height: 480px;
    &.short {
      max-height: 432px;
      @media (max-width: 764px) {
        height: calc(100vh - 194px);
        max-height: 100%;
      }
    }
    height: 70vh;
    background: #f2eeff;
    display: flex;
    flex-direction: column-reverse;
    padding: 0 8px;
    box-sizing: border-box;
    overflow-y: scroll;

    @media (max-width: 764px) {
      height: calc(100vh - 146px);
      max-height: 100%;
    }
  }
  .message-buttons {
    display: flex;
    padding: 8px 8px 4px 8px;
    background: #f2eeff;
    justify-content: flex-end;
    button {
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 14px;
      margin-right: 4px;
      background: none;
      border: 2px solid #916dd5;
      border-radius: 24px;
      color: #916dd5;
      &:last-child {
        margin-right: 0;
      }
    }
  }
  .message-input {
    display: flex;
    justify-content: center;
    height: 42px;
    position: relative;
    background: #f2eeff;
    padding: 12px 0 20px 0;

    @media (max-width: 764px) {
      // height: 64px;
    }
    input {
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
      width: 240px;
      border-radius: 20px;
      resize: none;
      border: none;
      font-size: 14px;
      padding: 12px 16px;
      margin-right: 6px;

      @media (max-width: 764px) {
        width: 60%;
      }
    }
    button {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 42px;
      background: #7E57C2;
      border-radius: 50%;
      border: none;
      outline: none;
      cursor: pointer;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);

      @media (max-width: 764px) {
        // width: 82px;
      }
      svg {
        position: absolute;
        height: 24px;
        width: 24px;
        fill: white;
        right: 10px;
      }
    }
  }
}
.fade-zoom-enter-active, .fade-zoom-leave-active {
  transition: all .1s ease;
}
.fade-zoom-enter, .fade-zoom-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
</style>
