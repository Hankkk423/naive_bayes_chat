console.log("js working");
// Get references to HTML elements
const chatButton = document.getElementById("chat-button");
const userInput = document.getElementById("user-input");
const chatLog = document.getElementById("chat-log");

const sendMessage = async () => {
    const message = userInput.value.trim();
    if (message !== '') {
        appendMessage_user(message, 'user-message');
        userInput.value = '';
  
        const response = await fetch('/to_model_NB', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
  
        const data = await response.json();
        const answer = data.res;
        
        console.log('input: ', message,
                '\ntag:', data.tag,
                '\nres: ', data.res);

        appendMessage_bot(answer, 'bot-message');
    }
};
    
// Append a message to the chat log
const appendMessage_user = (message, className) => {
    const messageElement = document.createElement("div");
    messageElement.classList.add(className);
    //messageElement.innerHTML = message;
    const bubbleElement = document.createElement("div");
    bubbleElement.classList.add("user-bubble");
    bubbleElement.textContent = message;

    messageElement.appendChild(bubbleElement);


    chatLog.appendChild(messageElement);

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Append a message to the chat log
const appendMessage_bot = (message, className) => {
    const messageElement = document.createElement("div");
    messageElement.classList.add(className);
    //messageElement.innerHTML = message;

    const botAvatar = document.createElement("div");
    botAvatar.classList.add("bot-avatar");
    // messageElement.appendChild(botAvatar);

    const bubbleElement = document.createElement("div");
    bubbleElement.classList.add("bot-bubble");
    bubbleElement.textContent = message;
    
    messageElement.appendChild(botAvatar);
    messageElement.appendChild(bubbleElement);


    chatLog.appendChild(messageElement);

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Event listener for user input
userInput.addEventListener("keydown", (event) => {
    if (event.keyCode === 13 || event.key === 'Enter') {
        console.log("event hit");
        sendMessage();
    }
    else{
        //appendMessage("something wrong", "user-message");
    }
});

chatButton.addEventListener("click", () => {
    const chatContainer = document.getElementById("chat-container");
    if (chatContainer.style.display === "none") {
        chatContainer.style.display = "block";
    } 
    else {
        chatContainer.style.display = "none";
    }
});

appendMessage_bot("Hello! How can I help you?", 'bot-message');
