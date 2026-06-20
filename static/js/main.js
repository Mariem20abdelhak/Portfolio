// Matrix rain background
(function () {
  const canvas = document.getElementById('bg-canvas');
  const ctx = canvas.getContext('2d');
  let cols, drops;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    cols = Math.floor(canvas.width / 18);
    drops = Array(cols).fill(1);
  }
  resize();
  window.addEventListener('resize', resize);

  const chars = '01アイウエオカキクケコサシスセソABCDEF<>{}[]/\\#@!$%?'.split('');

  setInterval(() => {
    ctx.fillStyle = 'rgba(8,12,9,0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00e676';
    ctx.font = '13px Space Mono, monospace';
    drops.forEach((y, i) => {
      ctx.fillText(chars[Math.floor(Math.random() * chars.length)], i * 18, y * 18);
      if (y * 18 > canvas.height && Math.random() > 0.978) drops[i] = 0;
      drops[i]++;
    });
  }, 55);
})();

// Terminal typewriter
(function () {
  const lines = [
    { type: 'cmd', prompt: 'mariem@portfolio:~$', text: ' whoami' },
    { type: 'out', text: 'full-stack developer · cybersecurity enthusiast' },
    { type: 'cmd', prompt: 'mariem@portfolio:~$', text: ' cat skills.txt' },
    { type: 'out', text: 'Python · Flask · WinDev · Spring Boot · Symfony', cls: 'c' },
    { type: 'cmd', prompt: 'mariem@portfolio:~$', text: ' nmap --open localhost' },
    { type: 'out', text: 'PORT     STATE  SERVICE' },
    { type: 'out', text: '5000/tcp open   flask', cls: 'c' },
    { type: 'cmd', prompt: 'mariem@portfolio:~$', text: ' echo $STATUS' },
    { type: 'out', text: 'AVAILABLE · REMOTE=YES · SEC_LEVEL=02', cls: 'c' },
    { type: 'cursor' },
  ];

  const body = document.getElementById('term-body');
  let li = 0, ci = 0;

  function renderLine(line) {
    const div = document.createElement('div');
    div.className = 'tl';
    if (line.type === 'cmd') {
      div.innerHTML = `<span class="prompt">${line.prompt}</span><span class="cmd">${line.text}</span>`;
    } else if (line.type === 'out') {
      div.innerHTML = `<span class="out${line.cls ? ' ' + line.cls : ''}">${line.text}</span>`;
    } else {
      div.innerHTML = `<span class="prompt">mariem@portfolio:~$</span> <span class="cursor"></span>`;
    }
    body.appendChild(div);
  }

  function typeNext() {
    if (li >= lines.length) return;
    const line = lines[li];
    if (line.type === 'cmd') {
      if (ci === 0) {
        const div = document.createElement('div');
        div.className = 'tl';
        div.innerHTML = `<span class="prompt">${line.prompt}</span><span class="cmd" id="typing-cmd"></span>`;
        body.appendChild(div);
      }
      const cmd = document.getElementById('typing-cmd');
      if (cmd && ci < line.text.length) {
        cmd.textContent += line.text[ci];
        ci++;
        setTimeout(typeNext, 55);
        return;
      }
      ci = 0; li++;
      setTimeout(typeNext, 200);
    } else {
      renderLine(line);
      li++;
      setTimeout(typeNext, line.type === 'cursor' ? 0 : 280);
    }
  }

  setTimeout(typeNext, 900);
})();

// Project filter
document.querySelectorAll('.filter').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    document.querySelectorAll('.project-card').forEach(card => {
      if (f === 'all' || card.dataset.cat === f) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
});

// Scroll reveal
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.project-card, .tl-item, .skill-group, .stat-card, .about-text p, .contact-text, .contact-box'
).forEach((el, i) => {
  el.classList.add('reveal');
  el.style.transitionDelay = `${(i % 4) * 0.07}s`;
  observer.observe(el);
});

// Nav active state on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 200) current = s.id;
  });
  navLinks.forEach(a => {
    a.style.color = a.getAttribute('href') === '#' + current
      ? 'var(--green)' : '';
  });
}, { passive: true });
