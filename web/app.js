const messages = {
  en: {
    brandTag: 'Money made clear', workspaceLabel: 'WORKSPACE', newWorkspace: 'New workspace',
    overview: 'Overview', transactions: 'Transactions', budgets: 'Budgets', recurring: 'Recurring',
    privateTitle: 'Private by design', privateText: 'Your data stays on this computer.', language: 'Language',
    financialWorkspace: 'FINANCIAL WORKSPACE', overviewSubtitle: 'A clear view of your month.',
    transactionsSubtitle: 'Every detail, in one place.', budgetsSubtitle: 'Give your money a plan.',
    recurringSubtitle: 'Stay ahead of regular payments.', month: 'Month', exportCsv: 'Export CSV',
    addTransaction: 'Add transaction', welcomeEyebrow: 'START HERE',
    welcomeTitle: 'Make room for better money decisions.',
    welcomeText: 'Create a family or business workspace to track income, expenses, budgets, and recurring costs in one place.',
    createWorkspace: 'Create workspace', workspacePlaceholder: 'e.g. Our home', categoryPlaceholder: 'e.g. Groceries', spendingSnapshot: 'SPENDING SNAPSHOT',
    whereMoneyGoes: 'Where your money goes', recentActivity: 'RECENT ACTIVITY',
    latestTransactions: 'Latest transactions', viewAll: 'View all', monthlyPlan: 'MONTHLY PLAN',
    budgetHealth: 'Budget health', manageBudgets: 'Manage budgets', activityLog: 'ACTIVITY LOG',
    allTransactions: 'All transactions', planAhead: 'PLAN AHEAD', monthlyBudgets: 'Monthly budgets',
    searchTransactions: 'Search category, person, or note', allTypes: 'All types', noMatches: 'No matching transactions.',
    budgetHint: 'Set a limit for each expense category. A zero amount removes a budget.',
    setBudget: 'Set budget', stayOnTop: 'STAY ON TOP', recurringTransactions: 'Recurring transactions',
    recurringHint: 'Automatically add monthly items on their due day. Past entries stay after a rule is removed.',
    addRecurring: 'Add recurring', getOrganized: 'GET ORGANIZED', workspaceName: 'Workspace name',
    workspaceType: 'Type', family: 'Family', business: 'Business', currency: 'Currency',
    currencyHint: 'Use one currency per workspace. Amounts are not converted.', cancel: 'Cancel',
    keepTrack: 'KEEP TRACK', type: 'Type', date: 'Date', amount: 'Amount', category: 'Category',
    personVendor: 'Person / vendor', personVendorPlaceholder: 'Who paid or received it?',
    noteReference: 'Note / reference', notePlaceholder: 'Optional details or invoice reference',
    saveTransaction: 'Save transaction', monthlyLimit: 'Monthly limit',
    budgetZeroHint: 'Enter 0 to remove an existing budget.', saveBudget: 'Save budget',
    automate: 'AUTOMATE', dayOfMonth: 'Day of month', startMonth: 'Start month',
    recurringDayHint: 'For short months, a 29th–31st due date falls on the last day.', saveRule: 'Save rule',
    income: 'Income', expense: 'Expense', balance: 'Balance', monthlyIncome: 'Money coming in',
    monthlyExpenses: 'Money going out', monthlyBalance: 'Income minus expenses',
    noExpenses: 'No expenses this month yet.', noTransactions: 'No transactions for this month.',
    noBudgets: 'No budgets for this month yet. Set one to start planning.',
    noRecurring: 'No recurring rules yet. Automate a monthly expense or income.',
    spent: 'Spent', left: 'Left', over: 'Over by', edit: 'Edit', delete: 'Delete',
    dateColumn: 'Date', categoryColumn: 'Category', typeColumn: 'Type',
    partyColumn: 'Person / vendor', amountColumn: 'Amount', actionsColumn: 'Actions',
    editTransaction: 'Edit transaction', deleteTransactionConfirm: 'Delete this transaction?',
    deleteRuleConfirm: 'Remove this recurring rule? Past transactions will stay.',
    saved: 'Saved successfully', deleted: 'Deleted successfully', exported: 'CSV downloaded',
    day: 'Day', since: 'since', everyMonth: 'Every month', entries: 'entries',
    familyCategories: ['Groceries', 'Housing', 'Utilities', 'Transport', 'Healthcare', 'Education', 'Dining', 'Entertainment', 'Salary', 'Other'],
    businessCategories: ['Rent', 'Software', 'Supplies', 'Travel', 'Marketing', 'Payroll', 'Taxes', 'Sales', 'Services', 'Other'],
  },
  fr: {
    brandTag: 'Vos finances, en clair', workspaceLabel: 'ESPACE', newWorkspace: 'Nouvel espace',
    overview: 'Vue générale', transactions: 'Opérations', budgets: 'Budgets', recurring: 'Récurrences',
    privateTitle: 'Confidentialité intégrée', privateText: 'Vos données restent sur cet ordinateur.', language: 'Langue',
    financialWorkspace: 'ESPACE FINANCIER', overviewSubtitle: 'Une vision claire de votre mois.',
    transactionsSubtitle: 'Tous les détails au même endroit.', budgetsSubtitle: 'Donnez un plan à votre argent.',
    recurringSubtitle: 'Anticipez les paiements réguliers.', month: 'Mois', exportCsv: 'Exporter CSV',
    addTransaction: 'Ajouter une opération', welcomeEyebrow: 'POUR COMMENCER',
    welcomeTitle: 'Prenez de meilleures décisions financières.',
    welcomeText: 'Créez un espace familial ou professionnel pour suivre revenus, dépenses, budgets et coûts récurrents.',
    createWorkspace: 'Créer un espace', workspacePlaceholder: 'ex. Notre foyer', categoryPlaceholder: 'ex. Courses', spendingSnapshot: 'DÉPENSES',
    whereMoneyGoes: 'Où va votre argent', recentActivity: 'ACTIVITÉ RÉCENTE',
    latestTransactions: 'Dernières opérations', viewAll: 'Tout voir', monthlyPlan: 'PLAN MENSUEL',
    budgetHealth: 'État des budgets', manageBudgets: 'Gérer les budgets', activityLog: 'HISTORIQUE',
    allTransactions: 'Toutes les opérations', planAhead: 'ANTICIPER', monthlyBudgets: 'Budgets mensuels',
    searchTransactions: 'Chercher une catégorie, personne ou note', allTypes: 'Tous les types', noMatches: 'Aucune opération correspondante.',
    budgetHint: 'Fixez une limite par catégorie de dépenses. Un montant nul supprime le budget.',
    setBudget: 'Définir un budget', stayOnTop: 'GARDER LE CAP', recurringTransactions: 'Opérations récurrentes',
    recurringHint: 'Ajoutez automatiquement les opérations à leur échéance. Les anciennes restent après suppression de la règle.',
    addRecurring: 'Ajouter une récurrence', getOrganized: 'S’ORGANISER', workspaceName: 'Nom de l’espace',
    workspaceType: 'Type', family: 'Famille', business: 'Entreprise', currency: 'Devise',
    currencyHint: 'Utilisez une seule devise par espace. Aucun taux de change n’est appliqué.', cancel: 'Annuler',
    keepTrack: 'SUIVI', type: 'Type', date: 'Date', amount: 'Montant', category: 'Catégorie',
    personVendor: 'Personne / fournisseur', personVendorPlaceholder: 'Qui a payé ou reçu ?',
    noteReference: 'Note / référence', notePlaceholder: 'Détails ou numéro de facture facultatifs',
    saveTransaction: 'Enregistrer', monthlyLimit: 'Limite mensuelle',
    budgetZeroHint: 'Saisissez 0 pour supprimer un budget.', saveBudget: 'Enregistrer le budget',
    automate: 'AUTOMATISER', dayOfMonth: 'Jour du mois', startMonth: 'Mois de début',
    recurringDayHint: 'Pour les mois courts, une échéance du 29 au 31 tombe le dernier jour.', saveRule: 'Enregistrer la règle',
    income: 'Revenus', expense: 'Dépenses', balance: 'Solde', monthlyIncome: 'Entrées d’argent',
    monthlyExpenses: 'Sorties d’argent', monthlyBalance: 'Revenus moins dépenses',
    noExpenses: 'Aucune dépense ce mois-ci.', noTransactions: 'Aucune opération ce mois-ci.',
    noBudgets: 'Aucun budget ce mois-ci. Définissez-en un pour commencer.',
    noRecurring: 'Aucune règle récurrente. Automatisez un revenu ou une dépense.',
    spent: 'Dépensé', left: 'Restant', over: 'Dépassement de', edit: 'Modifier', delete: 'Supprimer',
    dateColumn: 'Date', categoryColumn: 'Catégorie', typeColumn: 'Type',
    partyColumn: 'Personne / fournisseur', amountColumn: 'Montant', actionsColumn: 'Actions',
    editTransaction: 'Modifier l’opération', deleteTransactionConfirm: 'Supprimer cette opération ?',
    deleteRuleConfirm: 'Supprimer cette règle ? Les anciennes opérations resteront.',
    saved: 'Enregistré', deleted: 'Supprimé', exported: 'CSV téléchargé',
    day: 'Jour', since: 'depuis', everyMonth: 'Chaque mois', entries: 'opérations',
    familyCategories: ['Courses', 'Logement', 'Factures', 'Transport', 'Santé', 'Éducation', 'Restaurant', 'Loisirs', 'Salaire', 'Autre'],
    businessCategories: ['Loyer', 'Logiciels', 'Fournitures', 'Déplacements', 'Marketing', 'Salaires', 'Impôts', 'Ventes', 'Services', 'Autre'],
  },
  es: {
    brandTag: 'Tus finanzas, claras', workspaceLabel: 'ESPACIO', newWorkspace: 'Nuevo espacio',
    overview: 'Resumen', transactions: 'Movimientos', budgets: 'Presupuestos', recurring: 'Recurrentes',
    privateTitle: 'Privacidad por diseño', privateText: 'Tus datos permanecen en este ordenador.', language: 'Idioma',
    financialWorkspace: 'ESPACIO FINANCIERO', overviewSubtitle: 'Una vista clara de tu mes.',
    transactionsSubtitle: 'Cada detalle en un solo lugar.', budgetsSubtitle: 'Dale un plan a tu dinero.',
    recurringSubtitle: 'Adelántate a los pagos habituales.', month: 'Mes', exportCsv: 'Exportar CSV',
    addTransaction: 'Añadir movimiento', welcomeEyebrow: 'EMPIEZA AQUÍ',
    welcomeTitle: 'Toma mejores decisiones con tu dinero.',
    welcomeText: 'Crea un espacio familiar o de negocio para seguir ingresos, gastos, presupuestos y pagos recurrentes.',
    createWorkspace: 'Crear espacio', workspacePlaceholder: 'p. ej. Nuestro hogar', categoryPlaceholder: 'p. ej. Supermercado', spendingSnapshot: 'GASTOS',
    whereMoneyGoes: 'En qué gastas tu dinero', recentActivity: 'ACTIVIDAD RECIENTE',
    latestTransactions: 'Últimos movimientos', viewAll: 'Ver todo', monthlyPlan: 'PLAN MENSUAL',
    budgetHealth: 'Estado de presupuestos', manageBudgets: 'Gestionar presupuestos', activityLog: 'HISTORIAL',
    allTransactions: 'Todos los movimientos', planAhead: 'PLANIFICAR', monthlyBudgets: 'Presupuestos mensuales',
    searchTransactions: 'Buscar categoría, persona o nota', allTypes: 'Todos los tipos', noMatches: 'No hay movimientos coincidentes.',
    budgetHint: 'Fija un límite por categoría de gasto. Un importe de cero elimina el presupuesto.',
    setBudget: 'Fijar presupuesto', stayOnTop: 'AL DÍA', recurringTransactions: 'Movimientos recurrentes',
    recurringHint: 'Añade movimientos cada mes en la fecha prevista. Los anteriores permanecen al borrar una regla.',
    addRecurring: 'Añadir recurrente', getOrganized: 'ORGANÍZATE', workspaceName: 'Nombre del espacio',
    workspaceType: 'Tipo', family: 'Familia', business: 'Negocio', currency: 'Moneda',
    currencyHint: 'Usa una sola moneda por espacio. No se convierten importes.', cancel: 'Cancelar',
    keepTrack: 'REGISTRO', type: 'Tipo', date: 'Fecha', amount: 'Importe', category: 'Categoría',
    personVendor: 'Persona / proveedor', personVendorPlaceholder: '¿Quién pagó o cobró?',
    noteReference: 'Nota / referencia', notePlaceholder: 'Detalles o referencia de factura opcionales',
    saveTransaction: 'Guardar movimiento', monthlyLimit: 'Límite mensual',
    budgetZeroHint: 'Introduce 0 para quitar un presupuesto.', saveBudget: 'Guardar presupuesto',
    automate: 'AUTOMATIZAR', dayOfMonth: 'Día del mes', startMonth: 'Mes de inicio',
    recurringDayHint: 'En meses cortos, un vencimiento del 29 al 31 pasa al último día.', saveRule: 'Guardar regla',
    income: 'Ingresos', expense: 'Gastos', balance: 'Saldo', monthlyIncome: 'Dinero que entra',
    monthlyExpenses: 'Dinero que sale', monthlyBalance: 'Ingresos menos gastos',
    noExpenses: 'Todavía no hay gastos este mes.', noTransactions: 'No hay movimientos este mes.',
    noBudgets: 'Aún no hay presupuestos este mes. Crea uno para empezar.',
    noRecurring: 'Aún no hay reglas recurrentes. Automatiza un ingreso o gasto.',
    spent: 'Gastado', left: 'Restante', over: 'Superado por', edit: 'Editar', delete: 'Eliminar',
    dateColumn: 'Fecha', categoryColumn: 'Categoría', typeColumn: 'Tipo',
    partyColumn: 'Persona / proveedor', amountColumn: 'Importe', actionsColumn: 'Acciones',
    editTransaction: 'Editar movimiento', deleteTransactionConfirm: '¿Eliminar este movimiento?',
    deleteRuleConfirm: '¿Eliminar esta regla? Los movimientos anteriores permanecerán.',
    saved: 'Guardado', deleted: 'Eliminado', exported: 'CSV descargado',
    day: 'Día', since: 'desde', everyMonth: 'Cada mes', entries: 'movimientos',
    familyCategories: ['Supermercado', 'Vivienda', 'Servicios', 'Transporte', 'Salud', 'Educación', 'Restaurantes', 'Ocio', 'Salario', 'Otros'],
    businessCategories: ['Alquiler', 'Software', 'Suministros', 'Viajes', 'Marketing', 'Nóminas', 'Impuestos', 'Ventas', 'Servicios', 'Otros'],
  },
};

const $ = (selector) => document.querySelector(selector);
const localDate = () => {
  const value = new Date();
  return `${value.getFullYear()}-${String(value.getMonth() + 1).padStart(2, '0')}-${String(value.getDate()).padStart(2, '0')}`;
};
const state = {
  language: localStorage.getItem('masroofi-language') || 'en',
  month: localDate().slice(0, 7),
  workspaceId: Number(localStorage.getItem('masroofi-workspace')) || null,
  workspaces: [], dashboard: null, tab: 'overview', search: '', filter: 'all',
};
if (!messages[state.language]) state.language = 'en';
const t = (key) => messages[state.language][key] ?? messages.en[key] ?? key;
const locale = () => ({en: 'en-US', fr: 'fr-FR', es: 'es-ES'})[state.language];
const money = (cents) => new Intl.NumberFormat(locale(), {
  style: 'currency', currency: state.dashboard?.workspace.currency || 'EUR',
}).format(cents / 100);
const prettyDate = (value) => new Intl.DateTimeFormat(locale(), {day: 'numeric', month: 'short', year: 'numeric'}).format(new Date(`${value}T12:00:00`));
const escapeHtml = (value) => String(value ?? '').replace(/[&<>"']/g, (character) => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'})[character]);

async function api(path, options = {}) {
  const response = await fetch(path, {
    ...options,
    headers: options.body ? {'Content-Type': 'application/json'} : undefined,
    body: options.body ? JSON.stringify(options.body) : undefined,
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || `HTTP ${response.status}`);
  return result;
}

let toastTimer;
function toast(message, error = false) {
  const element = $('#toast');
  element.textContent = message;
  element.classList.toggle('error', error);
  element.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => element.classList.remove('show'), 3600);
}
function report(error) { toast(error.message || String(error), true); }

function translate() {
  document.documentElement.lang = state.language;
  document.querySelectorAll('[data-i18n]').forEach((element) => { element.textContent = t(element.dataset.i18n); });
  document.querySelectorAll('[data-i18n-placeholder]').forEach((element) => { element.placeholder = t(element.dataset.i18nPlaceholder); });
  document.querySelectorAll('[data-i18n-title]').forEach((element) => { element.title = t(element.dataset.i18nTitle); element.setAttribute('aria-label', t(element.dataset.i18nTitle)); });
  $('#language').value = state.language;
  $('#workspace-select').setAttribute('aria-label', t('workspaceLabel'));
  $('#transaction-search').setAttribute('aria-label', t('searchTransactions'));
  $('#transaction-filter').setAttribute('aria-label', t('type'));
  document.title = `Masroofi — ${t(state.tab)}`;
  $('#page-title').textContent = t(state.tab);
  $('#page-subtitle').textContent = t(`${state.tab}Subtitle`);
  $('#transaction-dialog-title').textContent = t($('#transaction-form').elements.id.value ? 'editTransaction' : 'addTransaction');
  updateCategorySuggestions();
  if (state.dashboard) renderDashboard();
  renderWorkspaceSelector();
}

function renderWorkspaceSelector() {
  const select = $('#workspace-select');
  select.innerHTML = state.workspaces.map((item) => `<option value="${item.id}">${escapeHtml(item.name)}</option>`).join('');
  if (state.workspaceId) select.value = String(state.workspaceId);
  const current = state.workspaces.find((item) => item.id === state.workspaceId);
  $('#workspace-kind').textContent = current ? `${t(current.kind)} · ${current.currency}` : '';
  $('#empty-workspaces').hidden = Boolean(current);
  $('#workspace-content').hidden = !current;
  $('#add-button').disabled = !current;
  $('#export-button').disabled = !current;
}

async function loadWorkspaces() {
  state.workspaces = (await api('/api/workspaces')).workspaces;
  if (!state.workspaces.some((item) => item.id === state.workspaceId)) {
    state.workspaceId = state.workspaces[0]?.id || null;
  }
  renderWorkspaceSelector();
  if (state.workspaceId) await refreshDashboard();
  else state.dashboard = null;
}

async function refreshDashboard() {
  if (!state.workspaceId) return;
  state.dashboard = await api(`/api/dashboard?workspace_id=${state.workspaceId}&month=${encodeURIComponent(state.month)}`);
  renderDashboard();
  updateCategorySuggestions();
}

function summaryCard(className, label, amount, foot) {
  return `<div class="summary-card ${className}"><div class="summary-label">${escapeHtml(label)}</div><div class="summary-amount">${escapeHtml(money(amount))}</div><div class="summary-foot">${escapeHtml(foot)}</div></div>`;
}

function renderDashboard() {
  const data = state.dashboard;
  if (!data) return;
  $('#summary-cards').innerHTML = [
    summaryCard('income', t('income'), data.income_cents, t('monthlyIncome')),
    summaryCard('expense', t('expense'), data.expense_cents, t('monthlyExpenses')),
    summaryCard('balance', t('balance'), data.balance_cents, t('monthlyBalance')),
  ].join('');

  const categories = Object.entries(data.spent_by_category).sort((a, b) => b[1] - a[1]);
  $('#category-breakdown').innerHTML = categories.length ? categories.slice(0, 6).map(([category, amount]) => {
    const width = Math.max(2, Math.round(amount / data.expense_cents * 100));
    return `<div class="category-row"><div class="category-top"><strong>${escapeHtml(category)}</strong><span>${escapeHtml(money(amount))}</span></div><div class="track"><div class="fill" style="width:${width}%"></div></div></div>`;
  }).join('') : `<div class="category-empty">${escapeHtml(t('noExpenses'))}</div>`;

  $('#recent-transactions').innerHTML = data.transactions.length ? data.transactions.slice(0, 5).map((item) => `
    <div class="recent-item"><div class="item-avatar ${item.kind}">${item.kind === 'income' ? '+' : '−'}</div>
    <div class="recent-main"><strong>${escapeHtml(item.category)}</strong><small>${escapeHtml(prettyDate(item.date))}${item.party ? ` · ${escapeHtml(item.party)}` : ''}</small></div>
    <span class="recent-amount ${item.kind}">${item.kind === 'expense' ? '−' : '+'}${escapeHtml(money(item.amount_cents))}</span></div>
  `).join('') : `<div class="category-empty">${escapeHtml(t('noTransactions'))}</div>`;

  $('#overview-budget-list').innerHTML = data.budgets.length ? data.budgets.slice(0, 3).map(budgetCard).join('') : `<div class="empty-panel">${escapeHtml(t('noBudgets'))}</div>`;
  $('#budget-list').innerHTML = data.budgets.length ? data.budgets.map(budgetCard).join('') : `<div class="surface empty-panel">${escapeHtml(t('noBudgets'))}</div>`;
  renderTransactions();
  $('#recurring-list').innerHTML = data.recurrences.length ? data.recurrences.map(ruleCard).join('') : `<div class="surface empty-panel">${escapeHtml(t('noRecurring'))}</div>`;
}

function renderTransactions() {
  const all = state.dashboard?.transactions || [];
  const query = state.search.trim().toLocaleLowerCase(locale());
  const rows = all.filter((item) => (state.filter === 'all' || item.kind === state.filter) &&
    (!query || [item.date, item.category, item.party, item.note].some((value) => value.toLocaleLowerCase(locale()).includes(query))));
  $('#transaction-count').textContent = `${rows.length} ${t('entries')}`;
  $('#transaction-list').innerHTML = rows.length ? transactionTable(rows) : `<div class="empty-panel">${escapeHtml(t(all.length ? 'noMatches' : 'noTransactions'))}</div>`;
}

function budgetCard(item) {
  const over = item.spent_cents > item.amount_cents;
  const width = Math.min(100, Math.round(item.spent_cents / item.amount_cents * 100));
  const difference = Math.abs(item.amount_cents - item.spent_cents);
  return `<div class="budget-card"><div class="category-top"><strong>${escapeHtml(item.category)}</strong><button class="budget-edit" type="button" data-action="budget-edit" data-category="${escapeHtml(item.category)}">${escapeHtml(t('edit'))}</button></div>
    <div class="track"><div class="fill ${over ? 'warn' : ''}" style="width:${width}%"></div></div>
    <div class="budget-meta ${over ? 'over' : ''}"><span>${escapeHtml(t('spent'))} ${escapeHtml(money(item.spent_cents))} / ${escapeHtml(money(item.amount_cents))}</span><span>${escapeHtml(t(over ? 'over' : 'left'))} ${escapeHtml(money(difference))}</span></div></div>`;
}

function transactionTable(rows) {
  return `<div class="table-wrap"><table class="data-table"><thead><tr>
    <th>${escapeHtml(t('dateColumn'))}</th><th>${escapeHtml(t('categoryColumn'))}</th><th>${escapeHtml(t('typeColumn'))}</th><th>${escapeHtml(t('partyColumn'))}</th><th>${escapeHtml(t('amountColumn'))}</th><th>${escapeHtml(t('actionsColumn'))}</th>
  </tr></thead><tbody>${rows.map((item) => `<tr>
    <td>${escapeHtml(prettyDate(item.date))}</td>
    <td><strong>${escapeHtml(item.category)}</strong>${item.note ? `<div class="tx-note" title="${escapeHtml(item.note)}">${escapeHtml(item.note)}</div>` : ''}</td>
    <td><span class="type-pill ${item.kind}">${escapeHtml(t(item.kind))}</span></td>
    <td>${escapeHtml(item.party || '—')}</td>
    <td class="amount-cell ${item.kind}">${item.kind === 'expense' ? '−' : '+'}${escapeHtml(money(item.amount_cents))}</td>
    <td><div class="row-actions"><button type="button" data-action="transaction-edit" data-id="${item.id}">${escapeHtml(t('edit'))}</button><button class="danger" type="button" data-action="transaction-delete" data-id="${item.id}">${escapeHtml(t('delete'))}</button></div></td>
  </tr>`).join('')}</tbody></table></div>`;
}

function ruleCard(item) {
  return `<div class="rule-card"><div class="rule-icon">↻</div><div class="rule-main"><strong>${escapeHtml(item.category)} · ${escapeHtml(t(item.kind))}</strong>
    <small>${escapeHtml(t('everyMonth'))} · ${escapeHtml(t('day'))} ${item.day} · ${escapeHtml(t('since'))} ${escapeHtml(item.start_month)}${item.party ? ` · ${escapeHtml(item.party)}` : ''}</small></div>
    <div class="rule-price">${escapeHtml(money(item.amount_cents))}</div><button class="danger-button" type="button" data-action="rule-delete" data-id="${item.id}">${escapeHtml(t('delete'))}</button></div>`;
}

function updateCategorySuggestions() {
  const defaults = messages[state.language][state.dashboard?.workspace.kind === 'business' ? 'businessCategories' : 'familyCategories'];
  const saved = state.dashboard ? [
    ...state.dashboard.transactions.map((item) => item.category),
    ...state.dashboard.budgets.map((item) => item.category),
    ...state.dashboard.recurrences.map((item) => item.category),
  ] : [];
  const options = [...new Set([...defaults, ...saved])].map((value) => `<option value="${escapeHtml(value)}"></option>`).join('');
  $('#categories').innerHTML = options;
  $('#budget-categories').innerHTML = options;
}

function switchTab(tab) {
  state.tab = tab;
  document.querySelectorAll('.panel').forEach((element) => element.classList.toggle('active', element.id === `${tab}-panel`));
  document.querySelectorAll('.nav-item').forEach((element) => element.classList.toggle('active', element.dataset.tab === tab));
  $('#page-title').textContent = t(tab);
  $('#page-subtitle').textContent = t(`${tab}Subtitle`);
  document.title = `Masroofi — ${t(tab)}`;
}

function openDialog(id) { $(`#${id}`).showModal(); }
function openTransaction(item = null) {
  const form = $('#transaction-form');
  form.reset();
  form.elements.id.value = item?.id || '';
  form.elements.kind.value = item?.kind || 'expense';
  form.elements.date.value = item?.date || localDate();
  form.elements.amount.value = item ? (item.amount_cents / 100).toFixed(2) : '';
  form.elements.category.value = item?.category || '';
  form.elements.party.value = item?.party || '';
  form.elements.note.value = item?.note || '';
  $('#transaction-dialog-title').textContent = t(item ? 'editTransaction' : 'addTransaction');
  openDialog('transaction-dialog');
}
function openBudget(item = null) {
  const form = $('#budget-form');
  form.reset();
  form.elements.category.value = item?.category || '';
  form.elements.amount.value = item ? (item.amount_cents / 100).toFixed(2) : '';
  openDialog('budget-dialog');
}
function openRecurring() {
  const form = $('#recurring-form');
  form.reset();
  form.elements.day.value = new Date().getDate();
  form.elements.start_month.value = state.month;
  openDialog('recurring-dialog');
}

async function exportCsv() {
  try {
    const response = await fetch(`/api/export?workspace_id=${state.workspaceId}&month=${encodeURIComponent(state.month)}`);
    if (!response.ok) throw new Error((await response.json()).error);
    const url = URL.createObjectURL(await response.blob());
    const link = document.createElement('a');
    link.href = url;
    link.download = `masroofi-${state.month}.csv`;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    toast(t('exported'));
  } catch (error) { report(error); }
}

document.addEventListener('click', async (event) => {
  const close = event.target.closest('[data-close]');
  if (close) { close.closest('dialog').close(); return; }
  const tabButton = event.target.closest('[data-tab]');
  if (tabButton) { switchTab(tabButton.dataset.tab); return; }
  const action = event.target.closest('[data-action]');
  if (!action) return;
  const id = Number(action.dataset.id);
  try {
    if (action.dataset.action === 'transaction-edit') {
      openTransaction(state.dashboard.transactions.find((item) => item.id === id));
    } else if (action.dataset.action === 'budget-edit') {
      openBudget(state.dashboard.budgets.find((item) => item.category === action.dataset.category));
    } else if (action.dataset.action === 'transaction-delete' && window.confirm(t('deleteTransactionConfirm'))) {
      await api(`/api/transactions/${id}?workspace_id=${state.workspaceId}`, {method: 'DELETE'});
      await refreshDashboard(); toast(t('deleted'));
    } else if (action.dataset.action === 'rule-delete' && window.confirm(t('deleteRuleConfirm'))) {
      await api(`/api/recurrences/${id}?workspace_id=${state.workspaceId}`, {method: 'DELETE'});
      await refreshDashboard(); toast(t('deleted'));
    }
  } catch (error) { report(error); }
});

$('#new-workspace').addEventListener('click', () => openDialog('workspace-dialog'));
$('#welcome-create').addEventListener('click', () => openDialog('workspace-dialog'));
$('#add-button').addEventListener('click', () => openTransaction());
$('#add-budget').addEventListener('click', () => openBudget());
$('#add-recurring').addEventListener('click', openRecurring);
$('#export-button').addEventListener('click', exportCsv);
$('#month').addEventListener('change', async (event) => {
  if (!event.target.value) return;
  state.month = event.target.value;
  try { await refreshDashboard(); } catch (error) { report(error); }
});
$('#transaction-search').addEventListener('input', (event) => {
  state.search = event.target.value;
  renderTransactions();
});
$('#transaction-filter').addEventListener('change', (event) => {
  state.filter = event.target.value;
  renderTransactions();
});
$('#workspace-select').addEventListener('change', async (event) => {
  state.workspaceId = Number(event.target.value);
  localStorage.setItem('masroofi-workspace', String(state.workspaceId));
  renderWorkspaceSelector();
  try { await refreshDashboard(); } catch (error) { report(error); }
});
$('#language').addEventListener('change', (event) => {
  state.language = event.target.value;
  localStorage.setItem('masroofi-language', state.language);
  translate();
});

$('#workspace-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(event.target));
  try {
    const created = await api('/api/workspaces', {method: 'POST', body: data});
    state.workspaceId = created.id;
    localStorage.setItem('masroofi-workspace', String(created.id));
    event.target.closest('dialog').close(); event.target.reset();
    await loadWorkspaces(); toast(t('saved'));
  } catch (error) { report(error); }
});
$('#transaction-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(event.target));
  const id = data.id;
  delete data.id;
  data.workspace_id = state.workspaceId;
  try {
    await api(id ? `/api/transactions/${id}` : '/api/transactions', {method: id ? 'PUT' : 'POST', body: data});
    event.target.closest('dialog').close();
    state.month = data.date.slice(0, 7); $('#month').value = state.month;
    await refreshDashboard(); toast(t('saved'));
  } catch (error) { report(error); }
});
$('#budget-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const data = {...Object.fromEntries(new FormData(event.target)), workspace_id: state.workspaceId, month: state.month};
  try {
    await api('/api/budgets', {method: 'PUT', body: data});
    event.target.closest('dialog').close(); await refreshDashboard(); toast(t('saved'));
  } catch (error) { report(error); }
});
$('#recurring-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const data = {...Object.fromEntries(new FormData(event.target)), workspace_id: state.workspaceId};
  try {
    await api('/api/recurrences', {method: 'POST', body: data});
    event.target.closest('dialog').close(); await refreshDashboard(); toast(t('saved'));
  } catch (error) { report(error); }
});

$('#month').value = state.month;
translate();
loadWorkspaces().catch(report);
