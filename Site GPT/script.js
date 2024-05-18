document.addEventListener("DOMContentLoaded", () => {
    const typingText = document.getElementById('typingText');
    const text = "Salut moi c'est Antonin";
    let index = 0;
    let direction = 1;
  
    function type() {
      typingText.textContent = text.slice(0, index);
      index += direction;
      if (index > text.length || index < 0) {
        direction *= -1;
        setTimeout(type, 1000); // Pause before changing direction
      } else {
        setTimeout(type, 200); // Speed of typing
      }
    }
  
    type();
  
    const letterContainer = document.getElementById('letter-container');
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  
    function createLetter() {
      const letter = document.createElement('div');
      letter.className = 'letter';
      letter.textContent = letters[Math.floor(Math.random() * letters.length)];
      letter.style.left = Math.random() * window.innerWidth + 'px';
      letter.style.animationDuration = (Math.random() * 3 + 7) + 's'; // Random duration within a longer range
      letterContainer.appendChild(letter);
  
      setTimeout(() => {
        letter.remove();
      }, 12000); // Increased timeout to allow letters to persist longer
    }
  
    setInterval(createLetter, 100); // Adjust interval for letter creation frequency
  
    // Scroll to summary section on arrow click
    const scrollArrow = document.getElementById('scrollArrow');
    const summarySection = document.getElementById('summarySection');
  
    scrollArrow.addEventListener('click', () => {
      scrollArrow.classList.add('clicked');
      summarySection.scrollIntoView({ behavior: 'smooth' });
  
      // Remove the class after some time to reset the color
      setTimeout(() => {
        scrollArrow.classList.remove('clicked');
      }, 1000); // Adjust the duration as needed
    });
  });