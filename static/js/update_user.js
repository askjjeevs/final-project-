const selectState = () => {
    const userStateList = document.querySelectorAll('#state > option')

    for (const state of userStateList) {
        if (state.value == userState) {
            state.setAttribute('selected', true);
        }
    }
}

selectState();