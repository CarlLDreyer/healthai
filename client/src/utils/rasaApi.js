import api from '@/utils/api'

export default {
  talkToBot (message) {
    let { text, sender } = message
    return api().post('/webhooks/rest/webhook', {
      sender: sender,
      message: text,
    })
  }
}
