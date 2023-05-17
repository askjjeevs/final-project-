function SubscribeActivity(props) {
    const myDiv = document.querySelector('#subscribe-section');
    const activityId = myDiv.getAttribute('data-activity-id');
    const logged_in_user = myDiv.getAttribute('data-logged-in-user');
    const logged_in_user_bool = (logged_in_user === 'true')
    const [isSubscribed, setIsSubscribed] = React.useState(logged_in_user_bool);
    
    const handleSubscribe = () => {
        fetch(`/subscribe/${activityId}`)
            .then((response) => response.json())
            .then((responseInfo) => {
                console.log(responseInfo);
                if (responseInfo['success'] === true) {
                    setIsSubscribed(true);
                } else {
                    alert(responseInfo['msg']);
                }
            });
    };
    return (
        <div>
            <button className="btn" onClick={handleSubscribe} disabled={isSubscribed}>
                {isSubscribed ? 'Subscribed' : 'Subscribe'}
            </button>
        </div>
    );

}
ReactDOM.render(<SubscribeActivity  />, document.querySelector('#subscribe-section'));

   

    
