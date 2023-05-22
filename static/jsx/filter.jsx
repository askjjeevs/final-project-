function FilterByActivity(props) {

    // const activityContainer = document.querySelector('#activities-to-filter');
    // const filterOption = document.querySelector('#activity-filter');
    // const activities = activityContainer.getAttribute('data-activities-to-filter');
    const fullActivityList = JSON.parse(activities);
    const [filteredActivities, setFilteredActivities] = React.useState(fullActivityList);

    //  filterItem = activity type selected
    const filterItem = (typeSelected) => {
            // for every activity in the full activity list the filter examines the contents of every activity and 
            // then returns the activity that matches the type selected
        const newFilteredActivities = fullActivityList.filter((activity) => {
            console.log(activity.activity_type, typeSelected)
            return activity.activity_type === typeSelected;
        });
        console.log(newFilteredActivities);
        setFilteredActivities(newFilteredActivities);
    };

    const activityTypes = [
        "Fitness/Exercise", 
        "Culinary", 
        "Art",
        "Entertainment",
        "Games/Gaming",
        "Outdoor",
        "Indoor",
        "Dancing",
        "Meditation",
        "Gardening",
        "DIY/Crafting",
        "Photography",
        "Shopping",
        "Volunteering",
        "Other"
     ]

    return (
        <div className="filter flex-container">
            <div className="left">
                {activityTypes.map((type, id) => {
                    return (
                        <div 
                        key={id} className="activity-btn">
                            
                            <button className="activity-filter" 
                                onClick={() => filterItem(type)}>
                                {type}
                            </button>
                        </div>
                    );
                })}
            </div>
            <div className="right-flex-container">
                {filteredActivities.map((activity, id) => {
                    return (
                        <div className="card act-card">                        
                            <div 
                                className=""
                                key={id}>
                                <img id="homepage-card-img" src={activity.activity_image_path} className="card-img-top" alt={activity.activity_name} />
                                <div className="card-body act-card-homepage-body">
                                <h5 className="h5 card-title"> 
                                    <a href={"/activities/" + activity.activity_id}>{activity.activity_name}</a>
                                </h5>
                                {/* <p className="card-text">{activity.activity_type}</p>
                                <p className="card-text">{activity.activity_date}</p> */}
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}
ReactDOM.render(<FilterByActivity />, document.querySelector('#activity-container'));
