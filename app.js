/**
 * STEM EdTech LMS - Single Page Application Core Controller
 * Self-contained Interactive Digital STEM Lesson Plan Architecture
 * (No media/thumbnails dependencies, Diversified Practice & Assessments)
 */

(function () {
  'use strict';

  // =========================================================================
  // Application State
  // =========================================================================
  const state = {
    data: [],                     // Loaded hierarchical dataset
    currentLevel: null,           // Selected Level Object (e.g., Mầm non, Tiểu học)
    currentLang: null,            // Selected Language ('VIE' or 'ENG')
    currentTopic: null,           // Selected Topic Object
    currentLecture: null,         // Selected Lecture Object
    currentStep: 1,               // 1: Bài học tương tác, 2: Thực hành, 3: Kiểm tra
    
    // Interactive Materials Checklist State
    checkedMaterials: new Set(),
    totalMaterialsCount: 0,

    // Practice Module State (4 Diversified Modes)
    practiceMode: 'flashcard',    // 'flashcard' | 'matching' | 'sequencing' | 'cloze'
    cardIndex: 0,
    cardFlipped: false,
    masteredCards: new Set(),
    
    // Matching Game State
    matchingSelectedTerm: null,
    matchingSelectedDef: null,
    matchedPairsCount: 0,

    // Step Sequencing State
    currentSequenceItems: [],
    
    // Quiz Module State (4 Diversified Question Types)
    quizSubmitted: false,
    quizAnswers: {},              // { questionIndex: chosenOptionText }
    quizScore: 0,

    // User LocalStorage Persistence
    completedLectures: new Set()
  };

  // =========================================================================
  // DOM Elements Cache
  // =========================================================================
  const DOM = {
    // Breadcrumb & Header
    breadcrumbList: document.getElementById('breadcrumb-list'),
    brandHomeBtn: document.getElementById('btn-brand-home'),
    completedCountBadge: document.getElementById('header-completed-count'),
    resetProgressBtn: document.getElementById('btn-theme-reset'),
    
    // Global Search
    searchInput: document.getElementById('global-search-input'),
    searchClearBtn: document.getElementById('search-clear-btn'),
    searchDropdown: document.getElementById('search-results-dropdown'),
    
    // Views
    viewLevels: document.getElementById('view-levels'),
    viewLanguages: document.getElementById('view-languages'),
    viewTopics: document.getElementById('view-topics'),
    viewLectures: document.getElementById('view-lectures'),
    viewLectureHub: document.getElementById('view-lecture-hub'),
    
    // Containers
    levelsContainer: document.getElementById('levels-container'),
    languagesContainer: document.getElementById('languages-container'),
    topicsContainer: document.getElementById('topics-container'),
    lecturesContainer: document.getElementById('lectures-container'),
    
    // Badges & Titles
    langLevelBadge: document.getElementById('lang-level-badge'),
    topicPathBadge: document.getElementById('topic-path-badge'),
    topicsTitle: document.getElementById('topics-title'),
    topicsDesc: document.getElementById('topics-desc'),
    lectureTopicBadge: document.getElementById('lecture-topic-badge'),
    lectureHeroIcon: document.getElementById('lecture-hero-icon'),
    lectureListTitle: document.getElementById('lecture-list-title'),
    lectureListDesc: document.getElementById('lecture-list-desc'),
    
    // Hub Header & Stepper
    hubLectureTitle: document.getElementById('hub-lecture-title'),
    hubFilePath: document.getElementById('hub-file-path'),
    hubCompletionStatus: document.getElementById('hub-completion-status'),
    stepBtn1: document.getElementById('step-btn-1'),
    stepBtn2: document.getElementById('step-btn-2'),
    stepBtn3: document.getElementById('step-btn-3'),
    stepContent1: document.getElementById('step-content-1'),
    stepContent2: document.getElementById('step-content-2'),
    stepContent3: document.getElementById('step-content-3'),
    
    // Step 1: Interactive Digital Lesson Elements
    lessonMetaDiscipline: document.getElementById('lesson-meta-discipline'),
    lessonMetaAge: document.getElementById('lesson-meta-age'),
    lessonMetaDuration: document.getElementById('lesson-meta-duration'),
    lessonMetaSummary: document.getElementById('lesson-meta-summary'),
    lessonPdfBox: document.getElementById('lesson-pdf-box'),
    pdfLabelTitle: document.getElementById('pdf-label-title'),
    lessonPdfFilename: document.getElementById('lesson-pdf-filename'),
    lessonPdfViewBtn: document.getElementById('lesson-pdf-view-btn'),
    lessonPdfDownloadBtn: document.getElementById('lesson-pdf-download-btn'),
    lessonObjectivesList: document.getElementById('lesson-objectives-list'),
    materialsProgressBadge: document.getElementById('materials-progress-badge'),
    matRequiredList: document.getElementById('mat-required-list'),
    matOptionalList: document.getElementById('mat-optional-list'),
    matToolsList: document.getElementById('mat-tools-list'),
    challengeScenarioText: document.getElementById('challenge-scenario-text'),
    challengeCriteriaList: document.getElementById('challenge-criteria-list'),
    challengeConstraintsList: document.getElementById('challenge-constraints-list'),
    sciencePrinciplesContainer: document.getElementById('science-principles-container'),
    edpStepsContainer: document.getElementById('edp-steps-container'),
    aiStepBadge: document.getElementById('ai-step-badge'),
    aiStepHeading: document.getElementById('ai-step-heading'),
    aiStepNarration: document.getElementById('ai-step-narration'),

    labCalcTitle: document.getElementById('lab-calc-title'),
    calcInput1Label: document.getElementById('calc-input1-label'),
    calcInput2Label: document.getElementById('calc-input2-label'),
    calcInput1: document.getElementById('calc-input-1'),
    calcInput2: document.getElementById('calc-input-2'),
    btnRunCalc: document.getElementById('btn-run-calc'),
    calcResultBox: document.getElementById('calc-result-box'),
    calcOutputValue: document.getElementById('calc-output-value'),
    calcOutputUnit: document.getElementById('calc-output-unit'),
    calcResultFeedback: document.getElementById('calc-result-feedback'),
    lessonDiscussionList: document.getElementById('lesson-discussion-list'),
    btnToggleAllAnswers: document.getElementById('btn-toggle-all-answers'),
    btnGotoStep2: document.getElementById('btn-goto-step-2'),
    
    // Step 2: Practice Elements (4 Modes)
    tabFlashcard: document.getElementById('tab-flashcard'),
    tabMatching: document.getElementById('tab-matching'),
    tabSequencing: document.getElementById('tab-sequencing'),
    tabCloze: document.getElementById('tab-cloze'),
    modeFlashcardView: document.getElementById('mode-flashcard-view'),
    modeMatchingView: document.getElementById('mode-matching-view'),
    modeSequencingView: document.getElementById('mode-sequencing-view'),
    modeClozeView: document.getElementById('mode-cloze-view'),
    practiceStatusBadge: document.getElementById('practice-status-badge'),
    
    // Flashcard
    flashcardCounter: document.getElementById('flashcard-counter'),
    activeFlashcard: document.getElementById('active-flashcard'),
    fcTerm: document.getElementById('fc-term'),
    fcPhonetic: document.getElementById('fc-phonetic'),
    fcDef: document.getElementById('fc-def'),
    fcExample: document.getElementById('fc-example'),
    fcPrevBtn: document.getElementById('fc-prev-btn'),
    fcFlipBtn: document.getElementById('fc-flip-btn'),
    fcNextBtn: document.getElementById('fc-next-btn'),
    fcMarkReview: document.getElementById('fc-mark-review'),
    fcMarkMastered: document.getElementById('fc-mark-mastered'),
    
    // Matching
    btnResetMatching: document.getElementById('btn-reset-matching'),
    colTermsList: document.getElementById('col-terms-list'),
    colDefsList: document.getElementById('col-defs-list'),
    matchingSuccessBanner: document.getElementById('matching-success-banner'),

    // Sequencing
    btnResetSequencing: document.getElementById('btn-reset-sequencing'),
    btnCheckSequencing: document.getElementById('btn-check-sequencing'),
    sequencingCardsContainer: document.getElementById('sequencing-cards-container'),
    sequencingFeedbackBanner: document.getElementById('sequencing-feedback-banner'),
    seqFeedbackTitle: document.getElementById('seq-feedback-title'),
    seqFeedbackDesc: document.getElementById('seq-feedback-desc'),

    // Cloze
    btnCheckCloze: document.getElementById('btn-check-cloze'),
    clozeItemsContainer: document.getElementById('cloze-items-container'),
    clozeFeedbackBanner: document.getElementById('cloze-feedback-banner'),
    clozeFeedbackTitle: document.getElementById('cloze-feedback-title'),
    clozeFeedbackDesc: document.getElementById('cloze-feedback-desc'),

    btnBackToStep1: document.getElementById('btn-back-to-step-1'),
    btnGotoStep3: document.getElementById('btn-goto-step-3'),
    
    // Step 3: Test Elements
    testResultBanner: document.getElementById('test-result-banner'),
    resultIcon: document.getElementById('result-icon'),
    resultTitle: document.getElementById('result-title'),
    resultDesc: document.getElementById('result-desc'),
    resultScoreText: document.getElementById('result-score-text'),
    resultPercentText: document.getElementById('result-percent-text'),
    resultStatusText: document.getElementById('result-status-text'),
    quizForm: document.getElementById('quiz-form'),
    quizProgressText: document.getElementById('quiz-progress-text'),
    quizQuestionsContainer: document.getElementById('quiz-questions-container'),
    btnSubmitQuiz: document.getElementById('btn-submit-quiz'),
    btnRetakeQuiz: document.getElementById('btn-retake-quiz'),
    btnNextLecture: document.getElementById('btn-next-lecture'),
    btnBackToStep2: document.getElementById('btn-back-to-step-2')
  };

  // =========================================================================
  // Initialization & Data Loading
  // =========================================================================
  async function init() {
    loadCompletedFromStorage();
    setupEventListeners();

    if (window.APP_DATA && Array.isArray(window.APP_DATA) && window.APP_DATA.length > 0) {
      state.data = window.APP_DATA;
      handleInitialRoute();
    } else {
      try {
        const response = await fetch('./data.json');
        if (response.ok) {
          state.data = await response.json();
          handleInitialRoute();
        } else {
          showFatalError('Không thể tải tệp data.json. Vui lòng kiểm tra data.js hoặc data.json trong thư mục.');
        }
      } catch (err) {
        showFatalError('Lỗi đọc dữ liệu: Hãy đảm bảo data.js được nạp trong index.html hoặc mở qua Local HTTP Server.');
      }
    }
  }

  function loadCompletedFromStorage() {
    try {
      const saved = localStorage.getItem('stem_completed_lectures');
      if (saved) {
        state.completedLectures = new Set(JSON.parse(saved));
      }
    } catch (e) {
      console.warn('LocalStorage not available');
    }
    updateCompletedCounter();
  }

  function saveCompletedToStorage() {
    try {
      localStorage.setItem('stem_completed_lectures', JSON.stringify(Array.from(state.completedLectures)));
    } catch (e) {}
    updateCompletedCounter();
  }

  function updateCompletedCounter() {
    if (DOM.completedCountBadge) {
      DOM.completedCountBadge.textContent = state.completedLectures.size;
    }
  }

  function showFatalError(msg) {
    if (DOM.levelsContainer) {
      DOM.levelsContainer.innerHTML = `<div class="card" style="padding: 2rem; color: var(--danger); text-align: center;"><h3>⚠️ ${msg}</h3></div>`;
    }
  }

  // =========================================================================
  // Navigation & Hash Routing
  // =========================================================================
  function switchView(viewName) {
    [DOM.viewLevels, DOM.viewLanguages, DOM.viewTopics, DOM.viewLectures, DOM.viewLectureHub].forEach(v => {
      if (v) v.classList.remove('active');
    });

    switch (viewName) {
      case 'levels':
        if (DOM.viewLevels) DOM.viewLevels.classList.add('active');
        renderBreadcrumbs();
        break;
      case 'languages':
        if (DOM.viewLanguages) DOM.viewLanguages.classList.add('active');
        renderBreadcrumbs();
        break;
      case 'topics':
        if (DOM.viewTopics) DOM.viewTopics.classList.add('active');
        renderBreadcrumbs();
        break;
      case 'lectures':
        if (DOM.viewLectures) DOM.viewLectures.classList.add('active');
        renderBreadcrumbs();
        break;
      case 'hub':
        if (DOM.viewLectureHub) DOM.viewLectureHub.classList.add('active');
        renderBreadcrumbs();
        break;
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
    updateUrlHash();
  }

  function updateUrlHash() {
    try {
      const params = new URLSearchParams();
      if (state.currentLevel) params.set('level', state.currentLevel.level);
      if (state.currentLang) params.set('lang', state.currentLang);
      if (state.currentTopic) params.set('topic', state.currentTopic.topicName);
      if (state.currentLecture) {
        params.set('lecture', state.currentLecture.lectureId);
        params.set('step', state.currentStep);
      }

      const queryStr = params.toString();
      if (window.history && window.history.replaceState) {
        if (queryStr) {
          window.history.replaceState(null, '', '#' + queryStr);
        } else {
          window.history.replaceState(null, '', window.location.pathname || window.location.href);
        }
      } else {
        window.location.hash = queryStr ? '#' + queryStr : '';
      }
    } catch (err) {
      // Graceful fallback for file:// protocol security restrictions
      try {
        const params = new URLSearchParams();
        if (state.currentLevel) params.set('level', state.currentLevel.level);
        if (state.currentLang) params.set('lang', state.currentLang);
        if (state.currentTopic) params.set('topic', state.currentTopic.topicName);
        if (state.currentLecture) {
          params.set('lecture', state.currentLecture.lectureId);
          params.set('step', state.currentStep);
        }
        const qs = params.toString();
        window.location.hash = qs ? '#' + qs : '';
      } catch (inner) {
        // Silently ignore hash update failure
      }
    }
  }

  function handleInitialRoute() {
    renderLevelsView();

    if (!window.location.hash) {
      switchView('levels');
      return;
    }

    try {
      const hash = window.location.hash.substring(1);
      const params = new URLSearchParams(hash);
      const levelName = params.get('level');
      const langCode = params.get('lang');
      const topicName = params.get('topic');
      const lectureId = params.get('lecture');
      const stepParam = parseInt(params.get('step') || '1', 10);

      if (levelName) {
        const foundLvl = state.data.find(l => l.level === levelName || l.levelFullName.includes(levelName));
        if (foundLvl) {
          selectLevel(foundLvl, false);
          if (langCode) {
            selectLanguage(langCode, false);
            if (topicName) {
              const langObj = state.currentLevel.languages.find(lg => lg.lang === state.currentLang);
              const foundTopic = langObj ? langObj.topics.find(t => t.topicName.trim().toLowerCase() === topicName.trim().toLowerCase()) : null;
              if (foundTopic) {
                selectTopic(foundTopic, false);
                if (lectureId) {
                  const foundLec = foundTopic.lectures.find(l => l.lectureId === lectureId);
                  if (foundLec) {
                    selectLecture(foundLec, stepParam, true);
                    return;
                  }
                }
                switchView('lectures');
                return;
              }
            }
            switchView('topics');
            return;
          }
          switchView('languages');
          return;
        }
      }
    } catch (e) {
      console.error('Route parsing error:', e);
    }

    switchView('levels');
  }

  // =========================================================================
  // Breadcrumb Component
  // =========================================================================
  function renderBreadcrumbs() {
    if (!DOM.breadcrumbList) return;
    DOM.breadcrumbList.innerHTML = '';

    const createCrumb = (label, onClick, isActive = false) => {
      const item = document.createElement('span');
      item.className = 'breadcrumb-item' + (isActive ? ' active' : '');
      item.textContent = label;
      if (!isActive && onClick) {
        item.addEventListener('click', onClick);
      }
      return item;
    };

    const createSep = () => {
      const sep = document.createElement('span');
      sep.className = 'breadcrumb-separator';
      sep.textContent = '›';
      return sep;
    };

    const isHomeActive = !state.currentLevel;
    DOM.breadcrumbList.appendChild(createCrumb('🏠 Trang chủ', () => {
      state.currentLevel = null;
      state.currentLang = null;
      state.currentTopic = null;
      state.currentLecture = null;
      switchView('levels');
    }, isHomeActive));

    if (state.currentLevel) {
      DOM.breadcrumbList.appendChild(createSep());
      const isLvlActive = !state.currentLang;
      DOM.breadcrumbList.appendChild(createCrumb(`${state.currentLevel.icon} ${state.currentLevel.level}`, () => {
        state.currentLang = null;
        state.currentTopic = null;
        state.currentLecture = null;
        renderLanguagesView();
        switchView('languages');
      }, isLvlActive));
    }

    if (state.currentLang) {
      DOM.breadcrumbList.appendChild(createSep());
      const isLangActive = !state.currentTopic;
      const langLabel = state.currentLang === 'VIE' ? '🇻🇳 Tiếng Việt' : '🇬🇧 English';
      DOM.breadcrumbList.appendChild(createCrumb(langLabel, () => {
        state.currentTopic = null;
        state.currentLecture = null;
        renderTopicsView();
        switchView('topics');
      }, isLangActive));
    }

    if (state.currentTopic) {
      DOM.breadcrumbList.appendChild(createSep());
      const isTopicActive = !state.currentLecture;
      DOM.breadcrumbList.appendChild(createCrumb(`${state.currentTopic.icon} ${state.currentTopic.topicName}`, () => {
        state.currentLecture = null;
        renderLecturesView();
        switchView('lectures');
      }, isTopicActive));
    }

    if (state.currentLecture) {
      DOM.breadcrumbList.appendChild(createSep());
      DOM.breadcrumbList.appendChild(createCrumb(state.currentLecture.title, null, true));
    }
  }

  // =========================================================================
  // View 1: Level Selection (Cấp học)
  // =========================================================================
  function renderLevelsView() {
    if (!DOM.levelsContainer) return;
    DOM.levelsContainer.innerHTML = '';

    state.data.forEach(lvl => {
      const card = document.createElement('div');
      card.className = 'level-card';
      
      const totalLectures = lvl.languages.reduce((acc, lg) => {
        return acc + lg.topics.reduce((tAcc, t) => tAcc + (t.lectures ? t.lectures.length : 0), 0);
      }, 0);

      card.innerHTML = `
        <div class="level-card-top">
          <div class="level-icon">${lvl.icon || '📚'}</div>
          <span class="level-age-badge">${lvl.ageGroup || ''}</span>
        </div>
        <h3 class="level-title">${lvl.levelFullName || lvl.level}</h3>
        <p class="level-desc">${lvl.description || ''}</p>
        <div class="level-footer">
          <div class="lang-tags">
            ${lvl.languages.map(lg => `<span class="lang-tag">${lg.lang}</span>`).join('')}
            <span class="lang-tag" style="background: var(--secondary-light); color: var(--secondary);">
              ${totalLectures} bài học
            </span>
          </div>
          <span class="btn-arrow-icon">➔</span>
        </div>
      `;

      card.addEventListener('click', () => selectLevel(lvl, true));
      DOM.levelsContainer.appendChild(card);
    });
  }

  function selectLevel(lvl, changeView = true) {
    state.currentLevel = lvl;
    state.currentLang = null;
    state.currentTopic = null;
    state.currentLecture = null;

    renderLanguagesView();
    if (changeView) switchView('languages');
  }

  // =========================================================================
  // View 2: Language Selection (Ngôn ngữ)
  // =========================================================================
  function renderLanguagesView() {
    if (!DOM.languagesContainer || !state.currentLevel) return;
    DOM.languagesContainer.innerHTML = '';

    if (DOM.langLevelBadge) {
      DOM.langLevelBadge.textContent = `${state.currentLevel.icon} ${state.currentLevel.levelFullName}`;
    }

    state.currentLevel.languages.forEach(lg => {
      const card = document.createElement('div');
      card.className = 'language-card';

      const isVie = lg.lang === 'VIE';
      const flagEmoji = isVie ? '🇻🇳' : '🇬🇧';
      const title = isVie ? 'Tiếng Việt (VIE)' : 'English (ENG)';
      const sub = isVie 
        ? 'Chương trình bài học số hóa chuẩn hóa tiếng Việt' 
        : 'Digital STEM interactive lessons in standard English';
      const count = lg.topics ? lg.topics.length : 0;

      card.innerHTML = `
        <div class="lang-flag">${flagEmoji}</div>
        <div class="lang-card-content">
          <h3 class="lang-card-title">${title}</h3>
          <p class="lang-card-subtitle">${sub}</p>
          <span class="lang-topic-count">📚 ${count} Chủ đề chuyên sâu</span>
        </div>
        <span class="btn-arrow-icon">➔</span>
      `;

      card.addEventListener('click', () => selectLanguage(lg.lang, true));
      DOM.languagesContainer.appendChild(card);
    });
  }

  function selectLanguage(langCode, changeView = true) {
    state.currentLang = langCode;
    state.currentTopic = null;
    state.currentLecture = null;

    renderTopicsView();
    if (changeView) switchView('topics');
  }

  // =========================================================================
  // View 3: Topic Selection (Chủ đề)
  // =========================================================================
  function renderTopicsView() {
    if (!DOM.topicsContainer || !state.currentLevel || !state.currentLang) return;
    DOM.topicsContainer.innerHTML = '';

    const langObj = state.currentLevel.languages.find(lg => lg.lang === state.currentLang);
    if (!langObj) return;

    if (DOM.topicPathBadge) {
      DOM.topicPathBadge.textContent = `${state.currentLevel.level} • ${state.currentLang}`;
    }

    if (DOM.topicsTitle) {
      DOM.topicsTitle.textContent = state.currentLang === 'VIE' 
        ? `Chủ Đề STEM - ${state.currentLevel.level}` 
        : `STEM Topics - ${state.currentLevel.level}`;
    }

    langObj.topics.forEach(top => {
      const card = document.createElement('div');
      card.className = 'topic-card';
      const lecCount = top.lectures ? top.lectures.length : 0;

      card.innerHTML = `
        <div class="topic-card-icon">${top.icon || '🔬'}</div>
        <h4 class="topic-card-name">${top.topicName}</h4>
        <p class="topic-card-desc">${top.description || 'Chuyên đề nghiên cứu và bài tập mô phỏng.'}</p>
        <div class="topic-card-footer">
          <span>📖 ${lecCount} Bài học số hóa</span>
          <span>Khám phá ➔</span>
        </div>
      `;

      card.addEventListener('click', () => selectTopic(top, true));
      DOM.topicsContainer.appendChild(card);
    });
  }

  function selectTopic(topicObj, changeView = true) {
    state.currentTopic = topicObj;
    state.currentLecture = null;

    renderLecturesView();
    if (changeView) switchView('lectures');
  }

  // =========================================================================
  // View 4: Lecture List (Clean Academic Cards - Media-free)
  // =========================================================================
  function renderLecturesView() {
    if (!DOM.lecturesContainer || !state.currentTopic) return;
    DOM.lecturesContainer.innerHTML = '';

    if (DOM.lectureTopicBadge) {
      DOM.lectureTopicBadge.textContent = `${state.currentLevel.level} / ${state.currentLang} / ${state.currentTopic.topicName}`;
    }
    if (DOM.lectureHeroIcon) {
      DOM.lectureHeroIcon.textContent = state.currentTopic.icon || '🔬';
    }
    if (DOM.lectureListTitle) {
      DOM.lectureListTitle.textContent = state.currentTopic.topicName;
    }
    if (DOM.lectureListDesc) {
      DOM.lectureListDesc.textContent = state.currentTopic.description || '';
    }

    state.currentTopic.lectures.forEach(lec => {
      const card = document.createElement('div');
      card.className = 'lecture-card';
      const isCompleted = state.completedLectures.has(lec.contentUrl || lec.lectureId);

      // Clean academic banner (replaces media image)
      card.innerHTML = `
        <div class="lecture-card-banner">
          <span class="lecture-card-id-pill">${lec.lectureId || 'Bài học'}</span>
          <span class="lecture-card-category-tag">${state.currentTopic.icon || '🔬'} ${state.currentTopic.topicName}</span>
        </div>
        <div class="lecture-card-body">
          <h4 class="lecture-card-title">${lec.title}</h4>
          <div class="lecture-features-row">
            <span class="feature-pill has-lesson">📋 Giáo án số hóa</span>
            <span class="feature-pill has-practice">🧩 4 Dạng thực hành</span>
            <span class="feature-pill has-quiz">📝 Kiểm tra đa dạng</span>
          </div>
          <div class="lecture-card-footer">
            <div class="lecture-done-indicator">
              ${isCompleted ? '<span>✅ Đã hoàn thành</span>' : '<span style="color: var(--text-muted);">○ Chưa hoàn thành</span>'}
            </div>
            <button type="button" class="btn btn-sm btn-primary btn-enter-lecture">Vào học ➔</button>
          </div>
        </div>
      `;

      card.addEventListener('click', () => selectLecture(lec, 1, true));
      const enterBtn = card.querySelector('.btn-enter-lecture');
      if (enterBtn) {
        enterBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          selectLecture(lec, 1, true);
        });
      }
      DOM.lecturesContainer.appendChild(card);
    });
  }

  function selectLecture(lecObj, step = 1, changeView = true) {
    if (!lecObj) return;
    state.currentLecture = lecObj;
    state.currentStep = step;
    state.checkedMaterials.clear();
    state.cardIndex = 0;
    state.cardFlipped = false;
    state.masteredCards.clear();
    state.quizSubmitted = false;
    state.quizAnswers = {};
    state.quizScore = 0;

    try {
      renderLectureHub();
    } catch (err) {
      console.error('Lỗi khi tải giao diện bài học:', err);
    }
    if (changeView) switchView('hub');
  }

  // =========================================================================
  // View 5: 3-Step Learning Hub
  // =========================================================================
  function renderLectureHub() {
    const lec = state.currentLecture;
    if (!lec) return;

    if (DOM.hubLectureTitle) DOM.hubLectureTitle.textContent = lec.title;
    if (DOM.hubFilePath) DOM.hubFilePath.textContent = `📋 Cấu trúc bài học số hóa chuẩn STEM EDP`;

    const isDone = state.completedLectures.has(lec.contentUrl || lec.lectureId);
    if (DOM.hubCompletionStatus) {
      if (isDone) {
        DOM.hubCompletionStatus.textContent = '✅ Đã hoàn thành';
        DOM.hubCompletionStatus.className = 'status-pill completed';
      } else {
        DOM.hubCompletionStatus.textContent = '○ Đang học';
        DOM.hubCompletionStatus.className = 'status-pill';
      }
    }

    // Step 1: Render Interactive Digital Lesson Plan
    renderDigitalLessonPlan(lec);

    // Step 2: Practice setup (4 Diversified Modes)
    setupPracticeModule();

    // Step 3: Test setup (4 Diversified Question Types)
    setupQuizModule();

    // Switch to current step
    goToStep(state.currentStep);
  }

  function goToStep(stepNum) {
    state.currentStep = stepNum;

    // Stepper header
    [DOM.stepBtn1, DOM.stepBtn2, DOM.stepBtn3].forEach((btn, idx) => {
      if (!btn) return;
      btn.classList.remove('active', 'completed');
      if (idx + 1 === stepNum) btn.classList.add('active');
      else if (idx + 1 < stepNum) btn.classList.add('completed');
    });

    // Content panels
    [DOM.stepContent1, DOM.stepContent2, DOM.stepContent3].forEach((cnt, idx) => {
      if (!cnt) return;
      if (idx + 1 === stepNum) cnt.classList.add('active');
      else cnt.classList.remove('active');
    });

    updateUrlHash();
    window.scrollTo({ top: 120, behavior: 'smooth' });
  }

  // =========================================================================
  // Module 1: Interactive Digital STEM Lesson Plan (Media-Free)
  // =========================================================================
  function renderDigitalLessonPlan(lec) {
    const lp = lec.lessonPlan || {};
    const overview = lp.overview || {};
    const materials = lp.materials || { required: [], optional: [], tools: [] };
    const challenge = lp.challenge || { scenario: '', criteria: [], constraints: [] };
    const principles = lp.scientificPrinciples || [];
    const steps = lp.engineeringSteps || [];
    const labCalc = lp.labCalculator || {};
    const discussions = lp.discussionQuestions || [];

    // 1. Meta Overview
    if (DOM.lessonMetaDiscipline) DOM.lessonMetaDiscipline.textContent = overview.discipline || 'Khoa học STEM';
    if (DOM.lessonMetaAge) DOM.lessonMetaAge.textContent = overview.ageGroup || '8 - 18 tuổi';
    if (DOM.lessonMetaDuration) DOM.lessonMetaDuration.textContent = overview.duration || '90 phút';
    if (DOM.lessonMetaSummary) DOM.lessonMetaSummary.textContent = overview.summary || lec.theoryNotes || '';

    // 1.1 Original Lesson Plan PDF Attachment
    if (DOM.lessonPdfBox) {
      const pdfPath = lec.contentUrl || '';
      const pdfName = lec.fileName || (pdfPath ? pdfPath.split('/').pop() : 'ke-hoach-bai-giang.pdf');
      const isEnglish = (state.currentLang === 'ENG' || (lec.id && lec.id.includes('_ENG_')));

      if (DOM.pdfLabelTitle) {
        DOM.pdfLabelTitle.textContent = isEnglish
          ? 'Original Lesson Plan Document (PDF Source):'
          : 'Tài liệu Kế hoạch Bài giảng (File PDF Gốc):';
      }
      if (DOM.lessonPdfFilename) {
        DOM.lessonPdfFilename.textContent = pdfName;
      }
      if (DOM.lessonPdfViewBtn) {
        DOM.lessonPdfViewBtn.href = pdfPath;
        DOM.lessonPdfViewBtn.innerHTML = isEnglish ? '<span>👁️ View PDF</span>' : '<span>👁️ Mở xem PDF</span>';
      }
      if (DOM.lessonPdfDownloadBtn) {
        DOM.lessonPdfDownloadBtn.href = pdfPath;
        DOM.lessonPdfDownloadBtn.setAttribute('download', pdfName);
        DOM.lessonPdfDownloadBtn.innerHTML = isEnglish ? '<span>⬇️ Download PDF</span>' : '<span>⬇️ Tải file về máy</span>';
      }
    }

    // 2. Objectives
    if (DOM.lessonObjectivesList) {
      const objs = lp.objectives || [
        "Nắm vững nguyên lý khoa học và kỹ thuật nền tảng của bài học.",
        "Áp dụng quy trình thiết kế kỹ thuật EDP để chế tạo mô hình thực tế.",
        "Đo lường các thông số thực nghiệm và đánh giá chất lượng sản phẩm."
      ];
      DOM.lessonObjectivesList.innerHTML = objs.map(o => `<li>${o}</li>`).join('');
    }

    // 3. Materials Checklist
    renderMaterialsChecklist(materials);

    // 4. Challenge (Scenario, Criteria, Constraints)
    if (DOM.challengeScenarioText) {
      DOM.challengeScenarioText.textContent = challenge.scenario || 'Giải quyết thử thách chế tạo mô hình thực nghiệm.';
    }
    if (DOM.challengeCriteriaList) {
      const crits = challenge.criteria || ["Mô hình tự hoạt động ổn định.", "Thu thập đủ số liệu thực nghiệm."];
      DOM.challengeCriteriaList.innerHTML = crits.map(c => `<li>${c}</li>`).join('');
    }
    if (DOM.challengeConstraintsList) {
      const constrs = challenge.constraints || ["Sử dụng vật liệu an toàn.", "Tuân thủ thời lượng quy định."];
      DOM.challengeConstraintsList.innerHTML = constrs.map(c => `<li>${c}</li>`).join('');
    }

    // 5. Scientific Principles
    if (DOM.sciencePrinciplesContainer) {
      if (principles.length > 0) {
        DOM.sciencePrinciplesContainer.innerHTML = principles.map(p => `
          <div class="principle-block">
            <h4 class="principle-title">🔬 ${p.title}</h4>
            <p class="principle-expl">${p.explanation}</p>
            ${p.formula ? `<div class="formula-callout">📐 Công thức: ${p.formula}</div>` : ''}
            ${p.realWorldApp ? `<p class="app-note"><strong>Ứng dụng thực tế:</strong> ${p.realWorldApp}</p>` : ''}
          </div>
        `).join('');
      } else {
        DOM.sciencePrinciplesContainer.innerHTML = `
          <div class="principle-block">
            <h4 class="principle-title">🔬 Nguyên lý Khoa học Cốt lõi</h4>
            <p class="principle-expl">${lec.theoryNotes || 'Khám phá các quy luật tự nhiên và ứng dụng kỹ thuật trong đời sống.'}</p>
          </div>
        `;
      }
    }

    // 6. 5-Step Engineering Design Process (EDP)
    if (DOM.edpStepsContainer) {
      if (steps.length > 0) {
        DOM.edpStepsContainer.innerHTML = steps.map(s => `
          <div class="edp-step-card">
            <div class="edp-step-num">${s.stepNumber}</div>
            <div class="edp-step-content">
              <h4 class="edp-step-name">${s.stepName}</h4>
              <p class="edp-step-inst">${s.instruction}</p>
              ${s.proTip ? `<span class="edp-pro-tip">💡 <strong>Mẹo Kỹ sư:</strong> ${s.proTip}</span>` : ''}
            </div>
          </div>
        `).join('');
      }
    }

    // 6.5 Video AI Minh Họa Quá Trình Thực Hiện (AI Process Video Simulation)

    // 7. Interactive STEM Lab Calculator
    setupLabCalculator(labCalc);

    // 8. Discussion Questions with Detailed Solutions
    renderDiscussionQA(discussions);
  }

  // Interactive Checklist Renderer
  function renderMaterialsChecklist(mats) {
    state.checkedMaterials.clear();
    let totalItems = 0;

    const renderList = (items, container) => {
      if (!container) return;
      if (!items || items.length === 0) {
        container.innerHTML = '<span style="font-size: 0.8rem; color: var(--text-muted);">Không yêu cầu</span>';
        return;
      }
      container.innerHTML = items.map((item, idx) => {
        const itemId = `mat_${idx}_${Math.random().toString(36).substring(2, 6)}`;
        totalItems++;
        return `
          <label class="mat-item-row" data-item="${itemId}">
            <input type="checkbox" class="mat-checkbox" data-id="${itemId}" />
            <span class="mat-item-label">${item}</span>
          </label>
        `;
      }).join('');
    };

    renderList(mats.required, DOM.matRequiredList);
    renderList(mats.optional, DOM.matOptionalList);
    renderList(mats.tools, DOM.matToolsList);

    state.totalMaterialsCount = totalItems;
    updateMaterialsProgressBadge();

    document.querySelectorAll('.mat-item-row').forEach(row => {
      const chk = row.querySelector('.mat-checkbox');
      chk.addEventListener('change', () => {
        const id = chk.dataset.id;
        if (chk.checked) {
          state.checkedMaterials.add(id);
          row.classList.add('checked');
        } else {
          state.checkedMaterials.delete(id);
          row.classList.remove('checked');
        }
        updateMaterialsProgressBadge();
      });
    });
  }

  function updateMaterialsProgressBadge() {
    if (!DOM.materialsProgressBadge) return;
    const count = state.checkedMaterials.size;
    const total = state.totalMaterialsCount;
    DOM.materialsProgressBadge.textContent = `${count}/${total} Đã chuẩn bị`;
    if (count === total && total > 0) {
      DOM.materialsProgressBadge.style.background = 'var(--success-light)';
      DOM.materialsProgressBadge.style.color = 'var(--success-hover)';
    } else {
      DOM.materialsProgressBadge.style.background = 'var(--primary-light)';
      DOM.materialsProgressBadge.style.color = 'var(--primary)';
    }
  }

  // Interactive STEM Lab Calculator Engine
  function setupLabCalculator(calcConfig) {
    if (!DOM.labCalcTitle) return;

    DOM.labCalcTitle.textContent = calcConfig.title || 'Bảng Tính Thực Nghiệm Tương Tác';
    if (DOM.calcInput1Label) DOM.calcInput1Label.textContent = (calcConfig.label1 || 'Thông số đo 1') + ':';
    if (DOM.calcInput2Label) DOM.calcInput2Label.textContent = (calcConfig.label2 || 'Thông số đo 2') + ':';
    if (DOM.calcOutputUnit) DOM.calcOutputUnit.textContent = calcConfig.unit || '';

    if (DOM.calcInput1) DOM.calcInput1.value = '';
    if (DOM.calcInput2) DOM.calcInput2.value = '';
    if (DOM.calcResultBox) DOM.calcResultBox.style.display = 'none';

    if (DOM.btnRunCalc) {
      DOM.btnRunCalc.onclick = () => {
        const v1 = parseFloat(DOM.calcInput1.value);
        const v2 = parseFloat(DOM.calcInput2.value);

        if (isNaN(v1) || isNaN(v2) || v2 <= 0) {
          alert('Vui lòng nhập số liệu thực nghiệm hợp lệ (thông số 2 phải lớn hơn 0)!');
          return;
        }

        let res = 0;
        let feedback = '';

        if (calcConfig.type === 'velocity') {
          res = v1 / v2;
          if (res > 2.0) feedback = '🚀 Tốc độ rất cao! Ma sát trục quay của xe bạn được triệt tiêu rất tốt.';
          else if (res >= 1.0) feedback = '✅ Vận tốc đạt chuẩn yêu cầu kỹ thuật. Sản phẩm vận hành ổn định.';
          else feedback = '⚠️ Tốc độ còn chậm. Hãy kiểm tra xem bánh xe có bị cọ xát vào khung gầm không.';
        } else if (calcConfig.type === 'bridge_ratio') {
          res = v1 / v2;
          if (res >= 50) feedback = '🌟 Xuất sắc! Cây cầu chịu được tải trọng gấp hơn 50 lần khối lượng bản thân!';
          else if (res >= 20) feedback = '✅ Kết cấu giàn tam giác phân tán lực rất tốt, đạt chuẩn thi đấu.';
          else feedback = '💡 Cần gia cố thêm các thanh chéo để tăng độ cứng vững của nhịp cầu.';
        } else if (calcConfig.type === 'power') {
          res = v1 * v2;
          feedback = `⚡ Công suất điện sinh ra: ${res.toFixed(3)} W. Đạt hiệu suất chuyển đổi năng lượng tốt.`;
        } else {
          res = (v1 / v2) * 100;
          feedback = `🎯 Hiệu suất mô hình đạt ${res.toFixed(1)}% so với mục tiêu lý thuyết đề ra.`;
        }

        if (DOM.calcOutputValue) DOM.calcOutputValue.textContent = res.toFixed(2);
        if (DOM.calcResultFeedback) DOM.calcResultFeedback.textContent = feedback;
        if (DOM.calcResultBox) DOM.calcResultBox.style.display = 'block';
      };
    }
  }

  // Section 1.7: Discussion Q&A Renderer (Interactive Cards with Engineer Solutions)
  function renderDiscussionQA(discussions) {
    if (!DOM.lessonDiscussionList) return;

    if (!discussions || discussions.length === 0) {
      DOM.lessonDiscussionList.innerHTML = '<p class="text-muted" style="padding: 1rem; text-align: center;">Chưa có câu hỏi thảo luận cho bài học này.</p>';
      return;
    }

    DOM.lessonDiscussionList.innerHTML = discussions.map((item, index) => {
      const qText = typeof item === 'object' && item.question ? item.question : item;
      const aText = typeof item === 'object' && item.answer 
        ? item.answer 
        : 'Hãy vận dụng tư duy 5 bước EDP và trao đổi cùng nhóm để tìm ra giải pháp tối ưu nhất cho thử thách này!';
      const itemId = `qa-item-${index}`;

      return `
        <div class="discussion-qa-card" id="${itemId}">
          <div class="qa-header" role="button" tabindex="0" aria-expanded="false" data-target="${itemId}">
            <div class="qa-question-box">
              <span class="qa-num-badge">Q${index + 1}</span>
              <span class="qa-question-text">${qText}</span>
            </div>
            <button type="button" class="qa-toggle-btn" aria-label="Xem gợi ý và lời giải">
              <span class="qa-btn-icon">👁️</span>
              <span class="qa-btn-text">Xem lời giải</span>
            </button>
          </div>
          <div class="qa-answer-box">
            <div class="qa-answer-title">
              <span>💡 Gợi ý & Lời giải từ Kỹ sư STEM:</span>
            </div>
            <div class="qa-answer-text">${aText}</div>
          </div>
        </div>
      `;
    }).join('');

    // Attach click listeners to cards and buttons
    DOM.lessonDiscussionList.querySelectorAll('.qa-header').forEach(header => {
      const handleToggle = () => {
        const card = header.closest('.discussion-qa-card');
        const btn = card.querySelector('.qa-toggle-btn');
        const isOpen = card.classList.toggle('open');
        header.setAttribute('aria-expanded', isOpen);
        if (btn) {
          const iconSpan = btn.querySelector('.qa-btn-icon');
          const textSpan = btn.querySelector('.qa-btn-text');
          if (iconSpan) iconSpan.textContent = isOpen ? '🙈' : '👁️';
          if (textSpan) textSpan.textContent = isOpen ? 'Ẩn lời giải' : 'Xem lời giải';
        }
      };

      header.addEventListener('click', handleToggle);
      header.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          handleToggle();
        }
      });
    });

    if (DOM.btnToggleAllAnswers) {
      DOM.btnToggleAllAnswers.textContent = '👁️ Hiện tất cả đáp án';
    }
  }

  function toggleAllDiscussionAnswers() {
    if (!DOM.lessonDiscussionList) return;
    const cards = DOM.lessonDiscussionList.querySelectorAll('.discussion-qa-card');
    if (cards.length === 0) return;

    // Check if any card is currently closed
    const hasClosed = Array.from(cards).some(card => !card.classList.contains('open'));

    cards.forEach(card => {
      const header = card.querySelector('.qa-header');
      const btn = card.querySelector('.qa-toggle-btn');
      if (hasClosed) {
        card.classList.add('open');
        if (header) header.setAttribute('aria-expanded', 'true');
        if (btn) {
          const iconSpan = btn.querySelector('.qa-btn-icon');
          const textSpan = btn.querySelector('.qa-btn-text');
          if (iconSpan) iconSpan.textContent = '🙈';
          if (textSpan) textSpan.textContent = 'Ẩn lời giải';
        }
      } else {
        card.classList.remove('open');
        if (header) header.setAttribute('aria-expanded', 'false');
        if (btn) {
          const iconSpan = btn.querySelector('.qa-btn-icon');
          const textSpan = btn.querySelector('.qa-btn-text');
          if (iconSpan) iconSpan.textContent = '👁️';
          if (textSpan) textSpan.textContent = 'Xem lời giải';
        }
      }
    });

    if (DOM.btnToggleAllAnswers) {
      DOM.btnToggleAllAnswers.textContent = hasClosed ? '🙈 Ẩn tất cả đáp án' : '👁️ Hiện tất cả đáp án';
    }
  }

  // =========================================================================
  // Module 2: Diversified Practice (4 Interactive Modes)
  // 1. Flashcards 3D, 2. Matching Game, 3. Step Sequencing, 4. Cloze Fill
  // =========================================================================
  function getPracticeDataSet() {
    const pData = state.currentLecture && state.currentLecture.practiceData;
    if (pData && pData.flashcards) {
      return pData;
    }
    // Fallback if array structure
    return {
      flashcards: [
        { term: "Khái niệm STEM", phonetic: "/ɛs tiː iː ɛm/", definition: "Tích hợp Khoa học, Công nghệ, Kỹ thuật và Toán học.", example: "Thực hành chế tạo giải quyết vấn đề." }
      ],
      matching: [
        { term: "Khái niệm STEM", definition: "Tích hợp Khoa học, Công nghệ, Kỹ thuật và Toán học." }
      ],
      sequencing: [
        { stepNumber: 1, text: "Xác định bài toán và các ràng buộc kỹ thuật" },
        { stepNumber: 2, text: "Đề xuất và phác thảo các ý tưởng thiết kế" },
        { stepNumber: 3, text: "Lập bản vẽ chi tiết và chuẩn bị vật liệu" },
        { stepNumber: 4, text: "Chế tạo mô hình mẫu thử nghiệm đầu tiên" },
        { stepNumber: 5, text: "Thử nghiệm, phân tích lỗi và cải tiến" }
      ],
      cloze: [
        { sentence: "Quy trình thiết kế kỹ thuật luôn bắt đầu bằng bước [...].", options: ["Hỏi & xác định vấn đề", "Mua vật liệu đắt nhất"], answer: "Hỏi & xác định vấn đề", explanation: "Làm rõ mục tiêu là bước tiên quyết." }
      ]
    };
  }

  function setupPracticeModule() {
    switchPracticeMode('flashcard');
    renderActiveFlashcard();
    setupMatchingGame();
    setupSequencingGame();
    setupClozeGame();
  }

  function switchPracticeMode(mode) {
    state.practiceMode = mode;
    [DOM.tabFlashcard, DOM.tabMatching, DOM.tabSequencing, DOM.tabCloze].forEach(tab => {
      if (!tab) return;
      tab.classList.toggle('active', tab.dataset.mode === mode);
    });

    [DOM.modeFlashcardView, DOM.modeMatchingView, DOM.modeSequencingView, DOM.modeClozeView].forEach(view => {
      if (!view) return;
      view.classList.remove('active');
    });

    if (mode === 'flashcard' && DOM.modeFlashcardView) DOM.modeFlashcardView.classList.add('active');
    else if (mode === 'matching' && DOM.modeMatchingView) DOM.modeMatchingView.classList.add('active');
    else if (mode === 'sequencing' && DOM.modeSequencingView) DOM.modeSequencingView.classList.add('active');
    else if (mode === 'cloze' && DOM.modeClozeView) DOM.modeClozeView.classList.add('active');
  }

  // --- Mode A: Flashcards ---
  function renderActiveFlashcard() {
    const data = getPracticeDataSet();
    const items = data.flashcards || [];
    if (items.length === 0) return;

    const item = items[state.cardIndex] || items[0];

    state.cardFlipped = false;
    if (DOM.activeFlashcard) DOM.activeFlashcard.classList.remove('flipped');

    const isVie = (state.currentLang || 'VIE') === 'VIE';
    if (DOM.flashcardCounter) {
      DOM.flashcardCounter.textContent = isVie 
        ? `Thẻ ${state.cardIndex + 1} / ${items.length}` 
        : `Card ${state.cardIndex + 1} / ${items.length}`;
    }

    const term = item.term || item.front || '';
    const def = item.definition || item.back || '';
    const phonetic = item.phonetic || '';
    const example = item.example || '';

    if (DOM.fcTerm) DOM.fcTerm.textContent = term;
    if (DOM.fcPhonetic) {
      DOM.fcPhonetic.textContent = phonetic;
      DOM.fcPhonetic.style.display = phonetic ? 'block' : 'none';
    }
    if (DOM.fcDef) DOM.fcDef.textContent = def;
    if (DOM.fcExample) {
      const exBox = DOM.fcExample.closest('.face-example-box');
      if (example) {
        DOM.fcExample.textContent = example;
        if (exBox) exBox.style.display = 'block';
      } else {
        if (exBox) exBox.style.display = 'none';
      }
    }

    if (DOM.practiceStatusBadge) {
      DOM.practiceStatusBadge.textContent = isVie 
        ? `Đã thuộc: ${state.masteredCards.size}/${items.length}` 
        : `Mastered: ${state.masteredCards.size}/${items.length}`;
    }
  }

  function flipFlashcard() {
    state.cardFlipped = !state.cardFlipped;
    if (DOM.activeFlashcard) {
      DOM.activeFlashcard.classList.toggle('flipped', state.cardFlipped);
    }
  }

  function nextFlashcard() {
    const items = getPracticeDataSet().flashcards || [];
    if (items.length === 0) return;
    state.cardIndex = (state.cardIndex + 1) % items.length;
    renderActiveFlashcard();
  }

  function prevFlashcard() {
    const items = getPracticeDataSet().flashcards || [];
    if (items.length === 0) return;
    state.cardIndex = (state.cardIndex - 1 + items.length) % items.length;
    renderActiveFlashcard();
  }

  // --- Mode B: Matching Game ---
  function setupMatchingGame() {
    if (!DOM.colTermsList || !DOM.colDefsList) return;

    DOM.colTermsList.innerHTML = '';
    DOM.colDefsList.innerHTML = '';
    if (DOM.matchingSuccessBanner) DOM.matchingSuccessBanner.style.display = 'none';

    state.matchingSelectedTerm = null;
    state.matchingSelectedDef = null;
    state.matchedPairsCount = 0;

    const pData = getPracticeDataSet();
    const items = pData.matching || pData.matchingPairs || [];
    const termCards = items.map((it, idx) => ({ id: idx, text: it.term || it.left || '' }));
    const defCards = items.map((it, idx) => ({ id: idx, text: it.definition || it.right || '' }));
    const shuffledDefs = [...defCards].sort(() => Math.random() - 0.5);

    termCards.forEach(tc => {
      const el = document.createElement('div');
      el.className = 'match-card';
      el.dataset.id = tc.id;
      el.textContent = tc.text;

      el.addEventListener('click', () => {
        if (el.classList.contains('matched')) return;
        DOM.colTermsList.querySelectorAll('.match-card').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        state.matchingSelectedTerm = tc.id;
        checkMatchingPair();
      });

      DOM.colTermsList.appendChild(el);
    });

    shuffledDefs.forEach(dc => {
      const el = document.createElement('div');
      el.className = 'match-card';
      el.dataset.id = dc.id;
      el.textContent = dc.text;

      el.addEventListener('click', () => {
        if (el.classList.contains('matched')) return;
        DOM.colDefsList.querySelectorAll('.match-card').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        state.matchingSelectedDef = dc.id;
        checkMatchingPair();
      });

      DOM.colDefsList.appendChild(el);
    });
  }

  function checkMatchingPair() {
    if (state.matchingSelectedTerm === null || state.matchingSelectedDef === null) {
      return;
    }

    const termEl = DOM.colTermsList.querySelector(`.match-card[data-id="${state.matchingSelectedTerm}"]`);
    const defEl = DOM.colDefsList.querySelector(`.match-card[data-id="${state.matchingSelectedDef}"]`);

    if (state.matchingSelectedTerm === state.matchingSelectedDef) {
      if (termEl) {
        termEl.classList.remove('selected');
        termEl.classList.add('matched');
        termEl.innerHTML = `✓ ${termEl.textContent}`;
      }
      if (defEl) {
        defEl.classList.remove('selected');
        defEl.classList.add('matched');
        defEl.innerHTML = `✓ ${defEl.textContent}`;
      }

      state.matchedPairsCount++;
      const pData = getPracticeDataSet();
      const items = pData.matching || pData.matchingPairs || [];
      if (state.matchedPairsCount >= items.length && items.length > 0) {
        if (DOM.matchingSuccessBanner) DOM.matchingSuccessBanner.style.display = 'flex';
      }

      state.matchingSelectedTerm = null;
      state.matchingSelectedDef = null;
    } else {
      if (termEl) termEl.classList.add('error-shake');
      if (defEl) defEl.classList.add('error-shake');

      setTimeout(() => {
        if (termEl) termEl.classList.remove('selected', 'error-shake');
        if (defEl) defEl.classList.remove('selected', 'error-shake');
        state.matchingSelectedTerm = null;
        state.matchingSelectedDef = null;
      }, 500);
    }
  }

  // --- Mode C: Step Sequencing Activity ---
  function setupSequencingGame() {
    if (!DOM.sequencingCardsContainer) return;
    if (DOM.sequencingFeedbackBanner) DOM.sequencingFeedbackBanner.style.display = 'none';

    const pData = getPracticeDataSet();
    const rawSteps = pData.sequencing || [];
    const normalizedSteps = rawSteps.map((step, idx) => {
      if (typeof step === 'string') {
        const match = step.match(/^(\d+)[\.:\s]+(.*)/);
        return {
          stepNumber: match ? parseInt(match[1], 10) : idx + 1,
          text: match ? match[2].trim() : step.trim()
        };
      }
      return {
        stepNumber: step.stepNumber || idx + 1,
        text: step.text || step.instruction || step.stepName || ''
      };
    });

    // Shuffle steps for the student to sort
    state.currentSequenceItems = [...normalizedSteps].sort(() => Math.random() - 0.5);
    renderSequencingCards();
  }

  function renderSequencingCards() {
    if (!DOM.sequencingCardsContainer) return;
    DOM.sequencingCardsContainer.innerHTML = '';

    state.currentSequenceItems.forEach((item, idx) => {
      const card = document.createElement('div');
      card.className = 'seq-card';
      card.dataset.idx = idx;

      const stepText = item.text || item.instruction || item.stepName || '';

      card.innerHTML = `
        <div class="seq-card-pos">${idx + 1}</div>
        <div class="seq-card-text">${stepText}</div>
        <div class="seq-card-actions">
          <button type="button" class="btn-move btn-move-up" ${idx === 0 ? 'disabled' : ''} title="Di chuyển lên">▲</button>
          <button type="button" class="btn-move btn-move-down" ${idx === state.currentSequenceItems.length - 1 ? 'disabled' : ''} title="Di chuyển xuống">▼</button>
        </div>
      `;

      // Up button
      const btnUp = card.querySelector('.btn-move-up');
      if (btnUp) {
        btnUp.addEventListener('click', (e) => {
          e.stopPropagation();
          if (idx > 0) {
            const temp = state.currentSequenceItems[idx];
            state.currentSequenceItems[idx] = state.currentSequenceItems[idx - 1];
            state.currentSequenceItems[idx - 1] = temp;
            renderSequencingCards();
          }
        });
      }

      // Down button
      const btnDown = card.querySelector('.btn-move-down');
      if (btnDown) {
        btnDown.addEventListener('click', (e) => {
          e.stopPropagation();
          if (idx < state.currentSequenceItems.length - 1) {
            const temp = state.currentSequenceItems[idx];
            state.currentSequenceItems[idx] = state.currentSequenceItems[idx + 1];
            state.currentSequenceItems[idx + 1] = temp;
            renderSequencingCards();
          }
        });
      }

      DOM.sequencingCardsContainer.appendChild(card);
    });
  }

  function checkSequencingResult() {
    let allCorrect = true;
    const cards = DOM.sequencingCardsContainer.querySelectorAll('.seq-card');
    const isVie = (state.currentLang || 'VIE') === 'VIE';

    state.currentSequenceItems.forEach((item, idx) => {
      const card = cards[idx];
      const isRightPos = (item.stepNumber === idx + 1);

      card.classList.remove('correct', 'wrong');
      if (isRightPos) {
        card.classList.add('correct');
      } else {
        card.classList.add('wrong');
        allCorrect = false;
      }
    });

    if (DOM.sequencingFeedbackBanner) {
      if (allCorrect) {
        DOM.seqFeedbackTitle.textContent = isVie ? '🎉 Tuyệt Vời! Trình Tự Hoàn Toàn Chính Xác!' : '🎉 Excellent! Sequence is Completely Correct!';
        DOM.seqFeedbackDesc.textContent = isVie ? 'Bạn đã nắm vững từng bước logic trong quy trình thực nghiệm kỹ thuật.' : 'You have mastered the logical sequence of the engineering design process.';
        DOM.sequencingFeedbackBanner.style.borderColor = 'var(--success)';
        DOM.sequencingFeedbackBanner.style.background = 'var(--success-light)';
      } else {
        DOM.seqFeedbackTitle.textContent = isVie ? '⚠️ Có Bước Chưa Đúng Vị Trí' : '⚠️ Some Steps are Out of Order';
        DOM.seqFeedbackDesc.textContent = isVie ? 'Hãy quan sát các thẻ màu đỏ và dùng nút mũi tên để đổi lại thứ tự theo logic thực nghiệm.' : 'Check the highlighted red cards and use arrow buttons to adjust the order.';
        DOM.sequencingFeedbackBanner.style.borderColor = 'var(--danger)';
        DOM.sequencingFeedbackBanner.style.background = 'var(--danger-light)';
      }
      DOM.sequencingFeedbackBanner.style.display = 'flex';
    }
  }

  // --- Mode D: Cloze Fill-in-the-blank Activity ---
  function setupClozeGame() {
    if (!DOM.clozeItemsContainer) return;
    DOM.clozeItemsContainer.innerHTML = '';
    if (DOM.clozeFeedbackBanner) DOM.clozeFeedbackBanner.style.display = 'none';

    const pData = getPracticeDataSet();
    const items = pData.cloze || [];
    const isVie = (state.currentLang || 'VIE') === 'VIE';

    // Collect all answers to build a unified word-bank options list
    const allAnswers = Array.from(new Set(items.map(it => (it.answer || '').trim()).filter(Boolean)));
    const fallbackVocab = isVie 
      ? ['tiêu chí', 'mẫu thử', 'cải tiến', 'giới hạn', 'thử nghiệm', 'tối ưu hóa', 'kỹ thuật', 'kết cấu']
      : ['criteria', 'prototype', 'iteration', 'constraints', 'testing', 'optimization', 'mechanics', 'structure'];

    items.forEach((item, idx) => {
      const card = document.createElement('div');
      card.className = 'cloze-card';
      card.id = `cloze-card-${idx}`;

      const rawSentence = item.sentence || item.text || '';
      const correctAnswer = (item.answer || '').trim();

      // Determine options list for this question
      let opts = [];
      if (item.options && Array.isArray(item.options) && item.options.length > 0) {
        opts = [...item.options];
      } else {
        const optSet = new Set();
        if (correctAnswer) optSet.add(correctAnswer);
        allAnswers.forEach(a => optSet.add(a));
        for (const word of fallbackVocab) {
          if (optSet.size >= 4) break;
          optSet.add(word);
        }
        opts = Array.from(optSet).sort(() => Math.random() - 0.5);
      }

      const optionsHtml = opts.map(opt => `<option value="${opt.replace(/"/g, '&quot;')}">${opt}</option>`).join('');

      const selectHtml = `
        <select class="cloze-select" id="cloze-sel-${idx}" data-answer="${correctAnswer.replace(/"/g, '&quot;')}">
          <option value="">-- ${isVie ? 'Chọn từ vựng' : 'Select Term'} --</option>
          ${optionsHtml}
        </select>
      `;

      // Replace gap: '_____', '____', '[...]', '[word]'
      let sentenceHtml = rawSentence;
      if (sentenceHtml.includes('_____')) {
        sentenceHtml = sentenceHtml.replace('_____', selectHtml);
      } else if (sentenceHtml.includes('[...]')) {
        sentenceHtml = sentenceHtml.replace('[...]', selectHtml);
      } else if (/_{3,}/.test(sentenceHtml)) {
        sentenceHtml = sentenceHtml.replace(/_{3,}/, selectHtml);
      } else if (/\[([^\]]+)\]/.test(sentenceHtml)) {
        sentenceHtml = sentenceHtml.replace(/\[([^\]]+)\]/, selectHtml);
      } else if (correctAnswer && sentenceHtml.toLowerCase().includes(correctAnswer.toLowerCase())) {
        const regex = new RegExp(correctAnswer.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
        sentenceHtml = sentenceHtml.replace(regex, selectHtml);
      } else {
        sentenceHtml = `${sentenceHtml} &nbsp; ${selectHtml}`;
      }

      const explText = item.explanation || (isVie 
        ? `Thuật ngữ chính xác: "${correctAnswer}". Giúp hoàn thiện ý nghĩa khoa học và kỹ thuật của mệnh đề.` 
        : `The correct engineering term is: "${correctAnswer}". It completes the technical meaning of the statement.`);

      card.innerHTML = `
        <div class="cloze-sentence">${idx + 1}. ${sentenceHtml}</div>
        <div class="cloze-expl" id="cloze-expl-${idx}" style="display: none;">
          💡 <strong>${isVie ? 'Giải thích' : 'Explanation'}:</strong> ${explText}
        </div>
      `;

      DOM.clozeItemsContainer.appendChild(card);
    });
  }

  function checkClozeResult() {
    const items = getPracticeDataSet().cloze || [];
    let correctCount = 0;
    let allSelected = true;

    items.forEach((item, idx) => {
      const sel = document.getElementById(`cloze-sel-${idx}`);
      const card = document.getElementById(`cloze-card-${idx}`);
      const expl = document.getElementById(`cloze-expl-${idx}`);
      if (!sel || !card) return;

      if (!sel.value) {
        allSelected = false;
        return;
      }

      const expected = (item.answer || sel.dataset.answer || '').trim().toLowerCase();
      const actual = sel.value.trim().toLowerCase();

      card.classList.remove('correct', 'wrong');
      if (actual === expected) {
        card.classList.add('correct');
        correctCount++;
      } else {
        card.classList.add('wrong');
      }

      if (expl) expl.style.display = 'block';
    });

    if (!allSelected) {
      alert('Vui lòng chọn từ vựng cho tất cả các câu trước khi kiểm tra!');
      return;
    }

    if (DOM.clozeFeedbackBanner) {
      if (correctCount === items.length) {
        DOM.clozeFeedbackTitle.textContent = `🎉 Hoàn Hảo! Đúng ${correctCount}/${items.length} Câu!`;
        DOM.clozeFeedbackDesc.textContent = 'Bạn đã sử dụng chuẩn xác các thuật ngữ khoa học và kỹ thuật chuyên ngành.';
        DOM.clozeFeedbackBanner.style.borderColor = 'var(--success)';
        DOM.clozeFeedbackBanner.style.background = 'var(--success-light)';
      } else {
        DOM.clozeFeedbackTitle.textContent = `Kết quả: Đúng ${correctCount}/${items.length} câu`;
        DOM.clozeFeedbackDesc.textContent = 'Đọc kỹ phần giải thích bên dưới các câu tô đỏ để củng cố lại kiến thức.';
        DOM.clozeFeedbackBanner.style.borderColor = 'var(--warning-border)';
        DOM.clozeFeedbackBanner.style.background = 'var(--warning-light)';
      }
      DOM.clozeFeedbackBanner.style.display = 'flex';
    }
  }

  // =========================================================================
  // Module 3: Diversified Assessments (4 Question Formats)
  // 1. Multiple Choice, 2. True/False, 3. Troubleshooting, 4. Calculation
  // =========================================================================
  function getNormalizedQuizData() {
    const raw = state.currentLecture && state.currentLecture.quizData;
    if (raw && Array.isArray(raw) && raw.length > 0) {
      return raw;
    }
    return [
      {
        type: "multiple_choice",
        badge: "🎯 Trắc nghiệm Nguyên lý",
        question: "Phương pháp học tập STEM chú trọng điều gì nhất?",
        options: [
          "Học thuộc lòng sách giáo khoa",
          "Tích hợp kiến thức thực tế và giải quyết vấn đề sáng tạo",
          "Chỉ làm bài kiểm tra trên giấy",
          "Không cần làm thí nghiệm"
        ],
        answer: "Tích hợp kiến thức thực tế và giải quyết vấn đề sáng tạo",
        explanation: "STEM nhấn mạnh sự gắn kết giữa lý thuyết và thực hành chế tạo giải quyết vấn đề thực tiễn."
      }
    ];
  }

  function setupQuizModule() {
    if (!DOM.quizQuestionsContainer) return;
    DOM.quizQuestionsContainer.innerHTML = '';

    if (DOM.testResultBanner) DOM.testResultBanner.style.display = 'none';
    if (DOM.btnSubmitQuiz) DOM.btnSubmitQuiz.style.display = 'inline-flex';
    if (DOM.btnRetakeQuiz) DOM.btnRetakeQuiz.style.display = 'none';
    if (DOM.btnNextLecture) DOM.btnNextLecture.style.display = 'none';

    const isVie = (state.currentLang || 'VIE') === 'VIE';
    const questions = getNormalizedQuizData();
    if (DOM.quizProgressText) {
      DOM.quizProgressText.textContent = isVie
        ? `Bộ câu hỏi đánh giá: ${questions.length} câu (Tích hợp Kỹ thuật, Toán học, Vật lý & Dữ liệu)`
        : `Assessment Evaluation: ${questions.length} Questions (Integrated Engineering, Physics & Math)`;
    }

    questions.forEach((q, qIdx) => {
      const qCard = document.createElement('div');
      qCard.className = 'question-card';
      qCard.id = `q-card-${qIdx}`;

      let badgeTypeClass = 'badge-engineering';
      const bText = q.badge || '';
      if (bText.includes('Vật lý') || bText.includes('Physics')) badgeTypeClass = 'badge-physics';
      else if (bText.includes('Toán') || bText.includes('Math') || bText.includes('Calculation')) badgeTypeClass = 'badge-math';
      else if (bText.includes('Sự cố') || bText.includes('Troubleshoot')) badgeTypeClass = 'badge-troubleshooting';
      else if (bText.includes('Vật liệu') || bText.includes('Materials')) badgeTypeClass = 'badge-materials';
      else if (bText.includes('Dữ liệu') || bText.includes('Data')) badgeTypeClass = 'badge-data';

      const badgeText = q.badge || (isVie ? '🎯 Kỹ thuật & Thiết kế' : '🎯 Engineering');

      qCard.innerHTML = `
        <span class="question-type-badge ${badgeTypeClass}">${badgeText}</span>
        <div class="question-title-row">
          <div class="question-num">${qIdx + 1}</div>
          <div class="question-text">${q.question}</div>
        </div>
        <div class="options-list">
          ${q.options.map((opt) => `
            <label class="option-item" data-qidx="${qIdx}">
              <input type="radio" name="q_${qIdx}" value="${opt.replace(/"/g, '&quot;')}" />
              <span class="option-label">${opt}</span>
              <span class="option-status-icon"></span>
            </label>
          `).join('')}
        </div>
        <div class="explanation-box" id="explanation-${qIdx}" style="display: none;">
          <strong>💡 ${isVie ? 'Phân tích từ Kỹ sư & Lời giải Toán/Vật lý:' : 'Engineering Analysis & Derivation:'}</strong>
          <p>${q.explanation || (isVie ? 'Đáp án chính xác dựa trên bài giảng lý thuyết.' : 'Correct answer based on technical principles.')}</p>
        </div>
      `;

      DOM.quizQuestionsContainer.appendChild(qCard);
    });
  }

  function handleQuizSubmit(e) {
    if (e) e.preventDefault();

    const questions = getNormalizedQuizData();
    let score = 0;
    let answeredAll = true;

    questions.forEach((q, qIdx) => {
      const checkedInput = DOM.quizForm.querySelector(`input[name="q_${qIdx}"]:checked`);
      const qCard = document.getElementById(`q-card-${qIdx}`);
      const explBox = document.getElementById(`explanation-${qIdx}`);

      if (!checkedInput) {
        answeredAll = false;
        if (qCard) qCard.style.borderColor = 'var(--danger)';
        return;
      }

      if (qCard) qCard.style.borderColor = 'var(--border)';
      const chosenValue = checkedInput.value;
      const isCorrect = (chosenValue.trim().toLowerCase() === q.answer.trim().toLowerCase());

      if (isCorrect) score++;

      const optionItems = qCard.querySelectorAll('.option-item');
      optionItems.forEach(item => {
        const input = item.querySelector('input');
        const iconSpan = item.querySelector('.option-status-icon');
        input.disabled = true;

        if (input.value.trim().toLowerCase() === q.answer.trim().toLowerCase()) {
          item.classList.add('correct-answer');
          if (iconSpan) {
            iconSpan.textContent = '✓';
            iconSpan.className = 'option-status-icon correct';
          }
        } else if (input.checked && !isCorrect) {
          item.classList.add('wrong-answer');
          if (iconSpan) {
            iconSpan.textContent = '✕';
            iconSpan.className = 'option-status-icon wrong';
          }
        }
      });

      if (explBox) explBox.style.display = 'block';
    });

    if (!answeredAll) {
      alert('Vui lòng trả lời đầy đủ tất cả các câu hỏi trước khi nộp bài!');
      return;
    }

    state.quizSubmitted = true;
    state.quizScore = score;

    const total = questions.length;
    const percent = Math.round((score / total) * 100);

    if (DOM.resultScoreText) DOM.resultScoreText.textContent = `${score}/${total}`;
    if (DOM.resultPercentText) DOM.resultPercentText.textContent = `${percent}%`;

    if (percent >= 60) {
      if (DOM.resultIcon) DOM.resultIcon.textContent = '🎉';
      if (DOM.resultTitle) DOM.resultTitle.textContent = isVie ? 'Xuất Sắc! Bạn Đã Vượt Qua Toàn Bộ Bài Đánh Giá' : 'Excellent! Assessment Completed Successfully';
      if (DOM.resultDesc) DOM.resultDesc.textContent = isVie 
        ? 'Bạn đã làm chủ cả lý thuyết vật lý, tư duy xử lý sự cố kỹ thuật và kỹ năng tính toán toán học thực nghiệm.'
        : 'You have mastered core physics principles, engineering troubleshooting, and applied mathematical calculations.';
      if (DOM.resultStatusText) {
        DOM.resultStatusText.textContent = isVie ? 'Đạt Yêu Cầu' : 'Passed';
        DOM.resultStatusText.style.color = 'var(--success)';
      }

      const lecKey = state.currentLecture.contentUrl || state.currentLecture.lectureId;
      state.completedLectures.add(lecKey);
      saveCompletedToStorage();

      if (DOM.hubCompletionStatus) {
        DOM.hubCompletionStatus.textContent = '✅ Đã hoàn thành';
        DOM.hubCompletionStatus.className = 'status-pill completed';
      }
    } else {
      if (DOM.resultIcon) DOM.resultIcon.textContent = '⚠️';
      if (DOM.resultTitle) DOM.resultTitle.textContent = isVie ? 'Cần Ôn Tập Thêm' : 'Review Needed';
      if (DOM.resultDesc) DOM.resultDesc.textContent = isVie 
        ? 'Hãy đọc kỹ phần phân tích của Kỹ sư bên dưới các câu sai và làm lại bài kiểm tra.'
        : 'Please review the engineering analysis under incorrect answers and retake the assessment.';
      if (DOM.resultStatusText) {
        DOM.resultStatusText.textContent = isVie ? 'Chưa Đạt' : 'Not Passed';
        DOM.resultStatusText.style.color = 'var(--danger)';
      }
    }

    if (DOM.testResultBanner) {
      DOM.testResultBanner.style.display = 'flex';
      DOM.testResultBanner.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    if (DOM.btnSubmitQuiz) DOM.btnSubmitQuiz.style.display = 'none';
    if (DOM.btnRetakeQuiz) DOM.btnRetakeQuiz.style.display = 'inline-flex';
    if (DOM.btnNextLecture) DOM.btnNextLecture.style.display = 'inline-flex';
  }

  function retakeQuiz() {
    setupQuizModule();
    window.scrollTo({ top: 120, behavior: 'smooth' });
  }

  function advanceToNextLecture() {
    if (!state.currentTopic || !state.currentTopic.lectures) return;
    const lecs = state.currentTopic.lectures;
    const currIdx = lecs.findIndex(l => l.lectureId === state.currentLecture.lectureId);
    if (currIdx >= 0 && currIdx < lecs.length - 1) {
      selectLecture(lecs[currIdx + 1], 1, true);
    } else {
      alert('Bạn đã hoàn thành bài học cuối cùng trong chủ đề này!');
      switchView('lectures');
    }
  }

  // =========================================================================
  // Global Search Engine
  // =========================================================================
  function handleSearchInput(e) {
    const val = e.target.value.trim().toLowerCase();
    if (!val) {
      if (DOM.searchClearBtn) DOM.searchClearBtn.style.display = 'none';
      if (DOM.searchDropdown) DOM.searchDropdown.style.display = 'none';
      return;
    }

    if (DOM.searchClearBtn) DOM.searchClearBtn.style.display = 'flex';

    const matches = [];
    state.data.forEach(lvl => {
      lvl.languages.forEach(lg => {
        lg.topics.forEach(t => {
          t.lectures.forEach(l => {
            if (
              l.title.toLowerCase().includes(val) ||
              t.topicName.toLowerCase().includes(val) ||
              (l.theoryNotes && l.theoryNotes.toLowerCase().includes(val))
            ) {
              matches.push({
                level: lvl,
                lang: lg.lang,
                topic: t,
                lecture: l
              });
            }
          });
        });
      });
    });

    renderSearchResults(matches.slice(0, 10));
  }

  function renderSearchResults(results) {
    if (!DOM.searchDropdown) return;

    if (results.length === 0) {
      DOM.searchDropdown.innerHTML = '<div class="search-result-item" style="color: var(--text-muted); cursor: default;">Không tìm thấy bài học nào phù hợp.</div>';
      DOM.searchDropdown.style.display = 'block';
      return;
    }

    DOM.searchDropdown.innerHTML = results.map((res, idx) => `
      <div class="search-result-item" data-idx="${idx}">
        <div class="search-result-title">${res.lecture.title}</div>
        <div class="search-result-meta">${res.level.level} • ${res.lang} • ${res.topic.topicName}</div>
      </div>
    `).join('');

    DOM.searchDropdown.querySelectorAll('.search-result-item').forEach((itemEl, idx) => {
      itemEl.addEventListener('click', () => {
        const item = results[idx];
        DOM.searchInput.value = '';
        DOM.searchDropdown.style.display = 'none';
        DOM.searchClearBtn.style.display = 'none';

        selectLevel(item.level, false);
        selectLanguage(item.lang, false);
        selectTopic(item.topic, false);
        selectLecture(item.lecture, 1, true);
      });
    });

    DOM.searchDropdown.style.display = 'block';
  }

  // =========================================================================
  // Global Event Listeners
  // =========================================================================
  function setupEventListeners() {
    if (DOM.brandHomeBtn) {
      DOM.brandHomeBtn.addEventListener('click', () => {
        state.currentLevel = null;
        state.currentLang = null;
        state.currentTopic = null;
        state.currentLecture = null;
        switchView('levels');
      });
    }

    if (DOM.resetProgressBtn) {
      DOM.resetProgressBtn.addEventListener('click', () => {
        if (confirm('Bạn có chắc muốn đặt lại toàn bộ tiến độ học tập?')) {
          state.completedLectures.clear();
          saveCompletedToStorage();
          if (state.currentLecture) renderLectureHub();
          else if (state.currentTopic) renderLecturesView();
        }
      });
    }

    document.querySelectorAll('.btn-back-step').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const target = e.currentTarget.dataset.target;
        if (target === 'levels') {
          state.currentLevel = null;
          state.currentLang = null;
          state.currentTopic = null;
          state.currentLecture = null;
          switchView('levels');
        } else if (target === 'languages') {
          state.currentLang = null;
          state.currentTopic = null;
          state.currentLecture = null;
          switchView('languages');
        } else if (target === 'topics') {
          state.currentTopic = null;
          state.currentLecture = null;
          switchView('topics');
        } else if (target === 'lectures') {
          state.currentLecture = null;
          switchView('lectures');
        }
      });
    });

    if (DOM.stepBtn1) DOM.stepBtn1.addEventListener('click', () => goToStep(1));
    if (DOM.stepBtn2) DOM.stepBtn2.addEventListener('click', () => goToStep(2));
    if (DOM.stepBtn3) DOM.stepBtn3.addEventListener('click', () => goToStep(3));

    if (DOM.btnGotoStep2) DOM.btnGotoStep2.addEventListener('click', () => goToStep(2));
    if (DOM.btnGotoStep3) DOM.btnGotoStep3.addEventListener('click', () => goToStep(3));
    if (DOM.btnBackToStep1) DOM.btnBackToStep1.addEventListener('click', () => goToStep(1));
    if (DOM.btnBackToStep2) DOM.btnBackToStep2.addEventListener('click', () => goToStep(2));

    if (DOM.btnToggleAllAnswers) {
      DOM.btnToggleAllAnswers.addEventListener('click', toggleAllDiscussionAnswers);
    }

    // Practice Mode Switcher
    if (DOM.tabFlashcard) DOM.tabFlashcard.addEventListener('click', () => switchPracticeMode('flashcard'));
    if (DOM.tabMatching) DOM.tabMatching.addEventListener('click', () => switchPracticeMode('matching'));
    if (DOM.tabSequencing) DOM.tabSequencing.addEventListener('click', () => switchPracticeMode('sequencing'));
    if (DOM.tabCloze) DOM.tabCloze.addEventListener('click', () => switchPracticeMode('cloze'));

    // Flashcard Controls
    if (DOM.activeFlashcard) DOM.activeFlashcard.addEventListener('click', flipFlashcard);
    if (DOM.fcFlipBtn) DOM.fcFlipBtn.addEventListener('click', flipFlashcard);
    if (DOM.fcNextBtn) DOM.fcNextBtn.addEventListener('click', nextFlashcard);
    if (DOM.fcPrevBtn) DOM.fcPrevBtn.addEventListener('click', prevFlashcard);

    if (DOM.fcMarkMastered) {
      DOM.fcMarkMastered.addEventListener('click', () => {
        state.masteredCards.add(state.cardIndex);
        renderActiveFlashcard();
        nextFlashcard();
      });
    }

    if (DOM.fcMarkReview) {
      DOM.fcMarkReview.addEventListener('click', () => {
        state.masteredCards.delete(state.cardIndex);
        renderActiveFlashcard();
        nextFlashcard();
      });
    }

    // Matching Controls
    if (DOM.btnResetMatching) DOM.btnResetMatching.addEventListener('click', setupMatchingGame);

    // Sequencing Controls
    if (DOM.btnResetSequencing) DOM.btnResetSequencing.addEventListener('click', setupSequencingGame);
    if (DOM.btnCheckSequencing) DOM.btnCheckSequencing.addEventListener('click', checkSequencingResult);

    // Cloze Controls
    if (DOM.btnCheckCloze) DOM.btnCheckCloze.addEventListener('click', checkClozeResult);

    // Quiz Controls
    if (DOM.quizForm) DOM.quizForm.addEventListener('submit', handleQuizSubmit);
    if (DOM.btnRetakeQuiz) DOM.btnRetakeQuiz.addEventListener('click', retakeQuiz);
    if (DOM.btnNextLecture) DOM.btnNextLecture.addEventListener('click', advanceToNextLecture);

    // Search Controls
    if (DOM.searchInput) DOM.searchInput.addEventListener('input', handleSearchInput);
    if (DOM.searchClearBtn) {
      DOM.searchClearBtn.addEventListener('click', () => {
        DOM.searchInput.value = '';
        DOM.searchClearBtn.style.display = 'none';
        if (DOM.searchDropdown) DOM.searchDropdown.style.display = 'none';
      });
    }

    // Keyboard Shortcuts (Space to flip flashcard, Arrow keys to navigate)
    document.addEventListener('keydown', (e) => {
      if (DOM.viewLectureHub && DOM.viewLectureHub.classList.contains('active') && state.currentStep === 2) {
        if (state.practiceMode === 'flashcard') {
          if (e.code === 'Space' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'SELECT' && e.target.tagName !== 'BUTTON') {
            e.preventDefault();
            flipFlashcard();
          } else if (e.code === 'ArrowRight') {
            nextFlashcard();
          } else if (e.code === 'ArrowLeft') {
            prevFlashcard();
          }
        }
      }
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-box')) {
        if (DOM.searchDropdown) DOM.searchDropdown.style.display = 'none';
      }
    });

    window.addEventListener('hashchange', handleInitialRoute);
  }

  // Expose internal controllers for tests and debugging
  window.appInternal = {
    state,
    selectLevel,
    selectLanguage,
    selectTopic,
    selectLecture,
    goToStep,
    switchView
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
