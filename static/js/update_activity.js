// js file to update the activity and state fields of the activity page. 
const insertActivityType = () =>{
    const userActivityList = document.querySelectorAll('#activity_type > option')

    for (const activity of userActivityList) {
        if (activity.value == activityType) {
            activity.setAttribute('selected', true);
        }
        
    }
}

insertActivityType();


// window.addEventListener("load", (event) => {
//     alert(activityType);

const insertState = () => {
    const activityStateList = document.querySelectorAll('#state > option')

    for (const state of activityStateList) {
        if (state.value == activityState) {
            state.setAttribute('selected', true);
        }
    }
}

insertState();
