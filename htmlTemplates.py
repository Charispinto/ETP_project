css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/1023581279377170513/1184552991915769866/header-chatbot-design.png?ex=658c63f1&is=6579eef1&hm=eb2116727ed2d823772a8a236dd91f214ccf35663e5af29035383adb73c0023b&" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static6.depositphotos.com/1003098/570/i/450/depositphotos_5701656-stock-photo-happy-friendly-woman.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
