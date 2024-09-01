const currentDate = document.queyrSelector(".current-date");
//getting new date, current year and month
let date = new Date(),
currYear = date.getFullYear(),
currMonth = date.getMonth();

const months  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

const renderCalendar = () => {
    let lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(); //getting last date of month
    let liTag = "";
    for (let i = 1; i <= lastDateofMonth; i++) {
        liTag = `<li>${i}</li>`;

    }
    //${months[currMonth]} ${currYear}
        currentDate.innerText = `sigma`;
        daysTag.innerHTML = liTag;

}
renderCalendar();