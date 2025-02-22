// Function to dynamically load subjects and mock papers
function loadSubjects(examType) {
    const subjects = {
        "Data Structures": ["Mid Term", "End Semester"],
        "Operating Systems": ["Internal Assessment", "End Semester"],
        "Database Management": ["Mid Term", "End Semester"],
        "Computer Networks": ["Internal Assessment", "End Semester"]
    };

    // Clear existing content
    const container = document.querySelector(".subject-container");
    container.innerHTML = "";

    // Display subjects dynamically
    for (let subject in subjects) {
        const subjectElement = document.createElement("div");
        subjectElement.className = "bg-white p-6 rounded shadow hover:bg-blue-100";
        subjectElement.innerHTML = `
            <h3 class="text-xl font-bold">${subject}</h3>
            <ul>
                ${subjects[subject]
                  .map(
                    exam =>
                      `<li class="text-gray-600 hover:text-blue-500 cursor-pointer">${exam}</li>`
                  )
                  .join("")}
            </ul>
        `;
        container.appendChild(subjectElement);
    }
}

// Function to display a popup when a subject is clicked (you can expand this later)
function displayPopup(subject, examType) {
    alert(`You selected ${subject} for ${examType}`);
}

// Add smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// Event listener to load subjects based on exam type
document.addEventListener("DOMContentLoaded", function () {
    const examLinks = document.querySelectorAll(".exam-link");
    examLinks.forEach(link => {
        link.addEventListener("click", function () {
            const examType = this.getAttribute("data-exam-type");
            loadSubjects(examType);
        });
    });
});





//lightbox effect
document.querySelectorAll('.image-gallery img').forEach(img => {
    img.addEventListener('click', () => {
        const lightbox = document.createElement('div');
        lightbox.classList.add('lightbox');
        document.body.appendChild(lightbox);

        const imgElement = document.createElement('img');
        imgElement.src = img.src;
        lightbox.appendChild(imgElement);

        lightbox.addEventListener('click', () => {
            lightbox.remove();
        });
    });
});

