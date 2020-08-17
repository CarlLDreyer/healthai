import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
/* eslint-disable */
export default new Vuex.Store({
  state: {
    chatOpen: false
  },
  mutations: {
    changeChatOpen (state, chatOpen) {
      state.chatOpen = chatOpen
    }
  },
  actions: {
    setChatOpen ({commit}, chatOpen) {
      commit('changeChatOpen', chatOpen)
    }
  },
  getters: {
    chatOpen: state => state.chatOpen
  }
})