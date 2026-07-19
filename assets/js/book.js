// Coding Interview Fight Club - Book
// Tab navigation for multi-language code samples

document.addEventListener('DOMContentLoaded', function() {
  initCodeTabs();
  initTOC();
  initFocusMode();
});

function initCodeTabs() {
  document.querySelectorAll('.code-tabs').forEach(function(tabs) {
    const buttons = tabs.querySelectorAll('.tab-btn');
    const contents = tabs.querySelectorAll('.tab-content');

    buttons.forEach(function(btn) {
      btn.addEventListener('click', function() {
        // Deactivate all
        buttons.forEach(b => b.classList.remove('active'));
        contents.forEach(c => c.classList.remove('active'));

        // Activate current
        btn.classList.add('active');
        const lang = btn.getAttribute('data-lang');
        const target = tabs.querySelector('.tab-content[data-lang="' + lang + '"]');
        if (target) target.classList.add('active');

        // Save preference
        try {
          localStorage.setItem('preferred-lang', lang);
        } catch(e) {}
      });
    });

    // Restore preference
    try {
      const preferred = localStorage.getItem('preferred-lang');
      if (preferred) {
        const btn = tabs.querySelector('.tab-btn[data-lang="' + preferred + '"]');
        if (btn) btn.click();
      }
    } catch(e) {}
  });
}

function initTOC() {
  const toc = document.querySelector('.toc');
  if (!toc) return;

  const headings = document.querySelector('.chapter-content').querySelectorAll('h2, h3');
  const list = toc.querySelector('ul') || document.createElement('ul');
  if (!toc.querySelector('ul')) toc.appendChild(list);

  headings.forEach(function(h) {
    if (!h.id) {
      h.id = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    }
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    a.className = 'toc-' + h.tagName.toLowerCase();
    li.appendChild(a);
    list.appendChild(li);
  });
}

function initFocusMode() {
  const toggle = document.getElementById('focus-toggle');
  if (!toggle) return;

  toggle.addEventListener('click', function() {
    document.body.classList.toggle('focus-mode');
    toggle.textContent = document.body.classList.contains('focus-mode')
      ? '🎯 Exit Focus Mode'
      : '🎯 Focus Mode';
  });
}

// Copy code button
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('pre').forEach(function(pre) {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = '📋 Copy';
    btn.style.cssText = 'position:absolute;top:0.5rem;right:0.5rem;padding:0.3rem 0.6rem;background:var(--bg-card);border:1px solid var(--border);border-radius:4px;color:var(--text-muted);cursor:pointer;font-size:0.75rem;z-index:10;';
    btn.addEventListener('click', function() {
      const code = pre.querySelector('code');
      const text = code ? code.textContent : pre.textContent;
      navigator.clipboard.writeText(text).then(function() {
        btn.textContent = '✅ Copied!';
        setTimeout(function() { btn.textContent = '📋 Copy'; }, 2000);
      });
    });
    pre.style.position = 'relative';
    pre.appendChild(btn);
  });
});
