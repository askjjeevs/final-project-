const subscribeButton = document.querySelector('#subscribe-button');

subscribeButton.addEventListener('click', (evt) => {
    const url = '/subscribe/' + subscribeButton.dataset.activityId;

    fetch(url)
    .then(response => response.json())
    .then(responseInfo => {
        alert(responseInfo);
        console.log(responseInfo);
        if (responseInfo['success'] == true){
            alert("success")
        } else {
            alert(responseInfo['msg']);
        }
    })

    alert(subscribeButton.dataset.activityId);
    console.log(evt);
  });
    