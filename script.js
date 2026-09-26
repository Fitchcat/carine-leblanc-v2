// Fallback for browsers that do not support modern CSS scroll-driven animations
if (!CSS.supports('(animation-timeline: view()) and (animation-range: entry)')) {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          // Optionnel: on peut dé-observer si on veut que l'animation ne joue qu'une fois
          // observer.unobserve(entry.target);
        }
      }
    },
    { 
      threshold: 0.15 // Se déclenche quand 15% de l'élément est visible
    }
  );

  document.querySelectorAll('.reveal').forEach((el) => {
    observer.observe(el);
  });
}

// Changement de style du header au scroll
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
  } else {
    header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.05)';
  }
});
