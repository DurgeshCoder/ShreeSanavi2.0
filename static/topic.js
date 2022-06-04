//get the unit details
function getUnitsOfSelectedCourse(selectedValue) {
    return fetch('/units_of_courses/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({'value': selectedValue})
    })
        .then(data => {
            return data.json()
        })
        .catch(error => {
            console.log(error)
        })

}

//ready events
document.addEventListener("DOMContentLoaded", () => {


    //adding the change event:
    let courseField = document.getElementById("id_course")
    courseField.addEventListener("change", (e) => {

        let selectedValue = e.target.value
        let unitField = document.getElementById("id_unit")
        unitField.innerHTML = ""
        getUnitsOfSelectedCourse(selectedValue).then(
            (data) => {

                JSON.parse(data).forEach(unit => {

                    let option = document.createElement("option")
                    option.value = unit.id
                    option.text = unit.title

                    unitField.add(option)

                })

            }
        )

    })


})