var socket = io();
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

function sendmessage(){
    date = new Date()
    var messagebody = {
        "body": document.getElementById("messagebox").value,
        "user" :  document.getElementById("usernamebox").value,
        "date": date
    }
    socket.emit("message_send", messagebody)
};
socket.on("message_recv", data => {
    var message = document.createElement("div");
    message.innerHTML = `<div class="message">${data["user"]}: ${data["body"]}<span></span></div>`
    document.getElementById("messages").appendChild(message)
    var element = document.getElementById("messages");
    var messageBody = document.querySelector('#messages');
    $(document).scrollTop($(document).height()); 
});
