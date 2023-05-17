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
        <div className="container-fluid">
            <h6>Filter By Activity Type:</h6>
            <div className="row justify-content-center">
                {activityTypes.map((type, id) => {
                    return (
                        <div 
                        key={id} className="activity-container">
                            
                            <button className="activity-filter" 
                                onClick={() => filterItem(type)}>
                                {type}
                            </button>
                        </div>
                    );
                })}
                {filteredActivities.map((activity, id) => {
                    return (
                        <div 
                            className="col-md-4 col-sm-6 card my-3 py-3 border-2"
                            key={id}>
                            <a href={"/activities/" + activity.activity_id}>{activity.activity_name}</a>
                            <p className="card-text">{activity.activity_type}</p>
                            <img src={activity.activity_image_path} className="card-img-top" alt={activity.activity_name} style={{ width: "200px", height: "200px" }} />
                            <p className="card-text">{activity.activity_date}</p>
                        </div>
                    );
                })}
            
            </div>
        </div>
    );

}
ReactDOM.render(<FilterByActivity />, document.querySelector('#activity-container'));
