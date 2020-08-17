class Message {
  constructor ({ text = '', sender = '', list, link, buttons } = {}) {
    this.text = text
    this.sender = sender
    if (list) this.list = list
    if (link) this.link = link
    if (buttons) this.buttons = buttons
    this.timestamp = +new Date()
  }
}

export default Message
