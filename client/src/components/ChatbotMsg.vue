<template>
  <div :class="`msg ${message.sender}`">
    <span class="avatar" :class="{'hidden': message.sender !== 'bot'}">
    </span>
    <span class="text" v-if="message.text">
      {{ message.text }}
      <span class="list" v-if="message.list">
        <ul>
          <li v-for="item in message.list" :key="item.id">{{ item }}</li>
        </ul>
      </span>
    </span>
    <span class="text link" v-if="message.link">
      <a :href="message.link.url" target="_blank">
        <span class="link-image" :style="{backgroundImage: 'url(' + message.link.image + ')'}">
        </span>
        <span class="link-text">
          <span class="title">{{ message.link.title }}</span>
          <span class="desc">{{ message.link.desc }}</span>
        </span>
      </a>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    message: {
      type: Object,
      required: true
    }
  },
}
</script>

<style lang="scss" scoped>
.msg {
  display: flex;
  position: relative;
  margin-bottom: 8px;
  &:last-child {
    padding-top: 16px;
  }
  span.avatar {
    display: block;
    height: 36px;
    width: 36px;
    border-radius: 50%;
    background: url('../assets/Avatar.png');
    background-size: cover;
    background-position: center;
  }
  span.text {
    display: block;
    background: white;
    max-width:calc(100% - 104px);
    padding: 12px 16px;
    box-sizing: border-box;
    font-size: 14px;
    line-height: 18px;
    border-radius: 24px;
    color: #080808;
    word-wrap: break-word;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    span.list {
      ul {
        padding-left: 24px;
        margin: 8px 0 0 0;
        font-size: 14px;
      }
    }
    &.link {
      cursor: pointer;
      padding: 0;
      a {
        text-decoration: none;
        .link-image {
          display: block;
          height: 140px;
          background-size: 110%;
          background-position: center;
          border-radius: 4px 14px 0 0;
          width: 240px;
        }
        .link-text {
          display: flex;
          flex-direction: column;
          padding: 12px 16px;
          .title {
            font-weight: 600;
            color: #080808;
          }
          .desc {
            font-size: 12px;
            color: #888888;
          }
        }
      }
    }
  }
  &.bot {
    text-align: left;
    &.first {
      margin-bottom: 6px;
      span.text {
        border-radius: 14px 14px 14px 4px;
      }
    }
    &.middle {
      margin-bottom: 6px;
      span.text {
        border-radius: 4px 14px 14px 4px;
      }
      span.avatar {
        background: none;
      }
    }
    &.last {
      span.text {
        border-radius: 4px 14px 14px 14px;
      }
      span.avatar {
        background: none;
      }
    }
    span.avatar {
      margin: -8px 8px 0 0;
    }
    span.text {
      border-radius: 4px 14px 14px 14px;
    }
  }
  &.user {
    text-align: right;
    flex-direction: row-reverse;
    &.first {
      margin-bottom: 6px;
      span.text {
        border-radius: 14px 14px 4px 14px;
      }
    }
    &.middle {
      margin-bottom: 6px;
      span.text {
        border-radius: 14px 4px 4px 14px;
      }
    }
    &.last {
      span.text {
        border-radius: 14px 4px 14px 14px;
      }
    }
    span.avatar {
      margin: -16px 0 0 8px;
      &.hidden {
        display: none;
      }
    }
    span.text {
      background: #D89CF6;
      color: white;
    }
  }
}
</style>
