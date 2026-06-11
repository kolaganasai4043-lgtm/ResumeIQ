async function analyzeResume() {
    var fileInput = document.getElementById('resumeFile');
    var jobRole = document.getElementById('jobRole').value;
    var loading = document.getElementById('loading');
    var results = document.getElementById('results');

    if (!fileInput.files[0]) {
        alert('Please upload a PDF resume!');
        return;
    }

    loading.style.display = 'block';
    results.style.display = 'none';

    var formData = new FormData();
    formData.append('resume', fileInput.files[0]);
    formData.append('job_role', jobRole);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        loading.style.display = 'none';
        results.style.display = 'block';
        results.innerHTML = '<div class="match-score">' + data.match_percentage + '%</div>'
            + '<div class="match-label">Job Match Score</div>'
            + '<div class="section"><h3>Skills Found</h3>'
            + data.extracted_skills.join(', ')
            + '</div><div class="section"><h3>Missing Skills</h3>'
            + data.missing_skills.join(', ')
            + '</div>';
    })
    .catch(function(error) {
        loading.style.display = 'none';
        alert('Error! Try again.');
    });
}