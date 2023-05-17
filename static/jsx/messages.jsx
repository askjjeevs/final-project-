function ActivityMessages() {
    const myDiv = document.querySelector('#subscribe-section');
    const activityId = myDiv.getAttribute('data-activity-id');    
    const [text, setText] = React.useState("");
    const [messages, setMessages] = React.useState([]);
    const [newMsgSumbitted, setNewMsgSumbitted] = React.useState(true);

    const handleSubmit = (event) => {
        event.preventDefault();
        
        const data = {
            "activity_id": activityId,
            "message_text": text
        }

        console.log(JSON.stringify(data))

        fetch('/messages', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => {
            if (response.status == 200) {
                setNewMsgSumbitted(!newMsgSumbitted);
            } else {
                console.log('Somthing happened wrong');
            }
        }).catch(err => err);
    };

    React.useEffect(() => {
        fetch('/messages/' + activityId)
            .then(response => response.json())
            .then(responseInfo => {
                const formatList = []
                for (const msg of responseInfo.messages) {
                    msg.created_datetime = 
                        moment(msg.created_datetime).format('MM-DD-YY, h:mm');
                    formatList.push(msg)
                }
                setMessages(formatList);
            });
    }, [newMsgSumbitted]);

    return (
        <div className="">
            <div className="messages-container">
                {messages.map((message, id) => {
                    return (
                        <div className="message flex-container"
                         key={id}>
                            <div className="message-image" >
                                <div> 
                                    <img src={message.user_image} className="img-thumbnail" style={{ width: "50px", height: "50px" }} />
                                </div>
                                <div className="username">{message.user_name}</div>
                                <div className="message-date">
                                    <div> {message.created_datetime} </div>
                                </div>                                  
                            </div>
                            <div className="message-text" >
                                <div> 
                                    {message.message_text}
                                </div>
                            </div>
                        </div>               
                    );
                })}               
            </div>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <textarea type="text"
                        placeholder="post your message here..."
                        value={text}
                        className="form-control post-message"
                        rows="5"
                        onChange={(evt) => setText(evt.target.value)}>
                    </textarea>
                </div>
                <input className="btn" type="submit" />
            </form>            
        </div>
    )
}

ReactDOM.render(<ActivityMessages />, document.querySelector('#activity-messages'));