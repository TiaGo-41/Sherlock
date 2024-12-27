function searchUsername() {
    const username = document.getElementById('username').value;
    const resultsList = document.getElementById('results-list');
    
    if (username === "") {
      alert("Veuillez entrer un pseudonyme.");
      return;
    }
    
    // Clear previous results
    resultsList.innerHTML = '';
    
    // Simulate searching (replace with actual functionality later)
    const fakeResults = [
      `Résultat 1 pour ${username} - Site 1`,
      `Résultat 2 pour ${username} - Site 2`,
      `Résultat 3 pour ${username} - Site 3`
    ];
    
    fakeResults.forEach(result => {
      const li = document.createElement('li');
      li.textContent = result;
      resultsList.appendChild(li);
    });
  }
  