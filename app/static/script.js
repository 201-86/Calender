const currentDate = document.querySelector(".current-date");
daysTag = document.querySelector(".days")
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
        currentDate.innerText = `${currMonth} ${currYear}`;
        daysTag.innerHTML = liTag;

}
renderCalendar();

prevNextIcon.forEach(icon => {
    icon.addEventListener("click", () => {
        //if clicked icon is previous icon then decrease currentmonth by 1 else increase by 1
        currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;
        renderCalendar();


    })
})