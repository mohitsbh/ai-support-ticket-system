---
name: Observability Ops
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#4b41e1'
  on-secondary: '#ffffff'
  secondary-container: '#645efb'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001e2f'
  on-tertiary-container: '#008cc7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#e2dfff'
  secondary-fixed-dim: '#c3c0ff'
  on-secondary-fixed: '#0f0069'
  on-secondary-fixed-variant: '#3323cc'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#89ceff'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
  surface-bg: '#F8FAFC'
  surface-card: '#FFFFFF'
  border-subtle: '#E2E8F0'
  border-strong: '#CBD5E1'
  status-critical: '#F43F5E'
  status-critical-subtle: '#FFF1F2'
  status-warning: '#F59E0B'
  status-warning-subtle: '#FFFBEB'
  status-success: '#10B981'
  status-success-subtle: '#ECFDF5'
  status-info: '#4F46E5'
  status-info-subtle: '#EEF2FF'
  badge-llm-text: '#7C3AED'
  badge-llm-bg: '#F5F3FF'
  badge-llm-border: '#DDD6FE'
  badge-rule-text: '#475569'
  badge-rule-bg: '#F1F5F9'
  badge-rule-border: '#E2E8F0'
typography:
  display-kpi:
    fontFamily: Geist
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Geist
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: -0.005em
  body-base:
    fontFamily: Geist
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0em
  label-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.02em
  label-mono-xs:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 12px
    letterSpacing: 0.04em
  table-cell-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  margin: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.5rem
---

## Brand & Style

The design system is engineered for support operations leads, platform reliability engineers, and technical leadership managing large-scale AI ticket pipelines. Its personality is utilitarian, hyper-focused, transparent, and authoritative. The interface evokes a sense of deep control, data clarity, and high-frequency precision reminiscent of modern monitoring consoles and developer-first task architectures.

The aesthetic follows an **Engineered Utilitarian** philosophy with high-density data framing:
- **Surface Rigor:** Clean, high-contrast structural hierarchy using crisp white surfaces nested within balanced slate boundaries, avoiding decorative clutter.
- **System Transparency:** Explicit technical provenance through dedicated execution badges (`[llm]` vs `[rule-based]`), monospaced code structures, and real-time query latency markers.
- **Actionable Semantics:** Strict reserve of vivid saturated tones for telemetry, anomalies, severity classifications, and SLA threshold violations, ensuring zero chromatic fatigue during all-day dashboard operations.

## Colors

The color palette prioritizes operational scanability and low cognitive overhead:

- **Structural Slate Hierarchy:** `#0F172A` (Slate 900) anchors all high-order typographic hierarchy, table headers, and critical numerical values. Intermediate neutrals (`#64748B` and `#475569`) handle supporting metadata, secondary metrics, and table column titles. `#F8FAFC` provides the foundational canvas wash to make `#FFFFFF` analytical cards stand out cleanly with structural `#E2E8F0` borders.
- **Brand / Focus Accents:** Primary interactions, selected tab indicators, active pagination states, and interactive filtering mechanisms utilize Indigo (`#4F46E5`) and Cyber Sky (`#0EA5E9`).
- **Semantic Alert Core:** Strict visual indicators mapped directly to system triage:
  - `status-critical` (`#F43F5E`): SLA breaches, escalated anomalies, and critical severity incident queues.
  - `status-warning` (`#F59E0B`): Approaching response time thresholds and ambiguous user sentiment drops.
  - `status-success` (`#10B981`): Autonomous resolution confirmations, healthy system throughput, and stable runtimes.
  - `status-info` (`#4F46E5`): In-progress routing, active agents, and live webhooks.
- **Engineered Provenance Tints:** Violet-tinted badge pairing (`#7C3AED` text on `#F5F3FF` background with `#DDD6FE` border) explicitly marks LLM-inferred outcomes, while neutral slate pill badges identify deterministic heuristic systems.

## Typography

The type system is split into two complementary technical engines:

- **Geist (Display & Interface Core):** Used across top-level views, metric values, navigation anchors, table records, and form labels. Optimized for extreme legibility at small sizes (12px–13px) and high information density. Tight kerning on display metrics (`display-kpi`) delivers immediate, commanding readouts without consuming excessive horizontal space.
- **JetBrains Mono (Technical Attribution & Metrics):** Applied systematically to all API routes (`/api/v1/tickets`), processing latency metrics (`142ms`), SQL/natural language tokens, model confidence figures, and ticket identification hashes (`#TCK-89211`). Monospaced alignment prevents vertical jitter across numeric table columns.

## Layout & Spacing

This design system employs a **dense fluid-grid framework** targeted at widescreen productivity:

- **Layout Structure:** Standard desktop view relies on a fixed left rail (collapsed at 64px, standard at 220px) coupled with a 12-column adaptive fluid canvas. Dashboard modules scale horizontally with a fixed gutter of `0.75rem` (12px), maximizing table footprint and chart resolution.
- **Density Scaling:** Vertical rhythm uses tightly stepped baseline increments. Metric cards enforce uniform `space-lg` (16px) internal padding, whereas tabular grid rows are compacted to 36px total height with `space-sm` (8px) internal padding to display maximum rows above the fold.
- **Reflow & Responsiveness:** Desktop-first design targeting views >= 1280px. Breakpoints down to 1024px collapse secondary multi-metric columns into stacked panels, while filters shift into a sliding parameter drawer.

## Elevation & Depth

Visual hierarchy is maintained through **crisp low-contrast outlines and micro-shadows**, prioritizing structural boundaries over heavy dimensional drop shadows:

- **Layer 0 (Canvas):** Pure `#F8FAFC` background acting as the foundational neutral bed.
- **Layer 1 (Cards & Data Panels):** Solid `#FFFFFF` fills strictly bordered by a 1px solid `#E2E8F0` rule. A minimal ambient drop shadow (`0 1px 2px 0 rgba(15, 23, 42, 0.04)`) separates primary analytical widgets from the canvas.
- **Layer 2 (Interactive Floating & Flyouts):** Dropdown selectors, date pickers, ticket preview drawers, and popover menus use elevated positioning (`0 4px 12px -2px rgba(15, 23, 42, 0.08), 0 2px 4px -1px rgba(15, 23, 42, 0.04)`) with `#CBD5E1` boundary definition.
- **Layer 3 (Command Palette & Incident Modals):** Central system overlays use backdrop dimming via `rgba(15, 23, 42, 0.4)` coupled with crisp modal containment (`0 20px 25px -5px rgba(15, 23, 42, 0.1)`).

## Shapes

The design system implements a **Soft (Level 1)** geometric specification to mirror modern high-efficiency developer tooling:

- **Cards & Data Grids:** 6px (`0.375rem`) border-radius for balanced, technical containment.
- **Form Controls & Inputs:** 4px (`0.25rem`) corner radius to preserve tight structural rhythm and sharp vertical alignment.
- **Execution Mode & Attribution Badges:** Fully rounded pill format (`9999px`) used exclusively for semantic tags (e.g., `[llm]`, `[rule-based]`, `Open`, `Critical`) to visually distinguish status metadata from interactive rectangular controls.

## Components

### Buttons
- **Primary:** `#0F172A` fill with `#FFFFFF` text, 4px corner radius, 32px height in standard density (`px-3 py-1.5`). Hover transitions to `#1E293B`.
- **Secondary:** `#FFFFFF` fill, 1px solid `#E2E8F0` border, `#0F172A` text. Hover brings a crisp surface shift to `#F8FAFC` and border tint to `#CBD5E1`.
- **Destructive/Escalation:** `#FFF1F2` fill, 1px solid `#FECDD3` border, `#E11D48` text. Hover shifts to `#FFE4E6`.

### Provenance & Status Chips
- **Execution Mode (`[llm]`):** Pill badge with `badge-llm-bg` fill, `badge-llm-border` border, and `badge-llm-text` font rendering in `label-mono-xs`.
- **Execution Mode (`[rule-based]`):** Pill badge with `badge-rule-bg` fill, `badge-rule-border` border, and `badge-rule-text` font rendering in `label-mono-xs`.
- **Severity Badges:** High-contrast indicator dot (6px) paired with uppercase alphanumeric labels (`CRITICAL`, `ELEVATED`, `NORMAL`).

### Data Tables
- **Header:** Height 32px, text styled in `label-mono-sm` using `#64748B`, uppercase, tracking-wider, bottom border 1px solid `#E2E8F0`.
- **Rows:** 36px fixed height for ultra-dense monitoring. Alternating transparent/subtle white hover state (`#F8FAFC`). All IDs, status chips, and latency readouts use monospaced figures aligned tabularly.

### Metric / KPI Cards
- **Structure:** Crisp `#FFFFFF` card, 1px solid `#E2E8F0`, interior padding `space-lg`.
- **Layout:** Micro-label header in `label-mono-xs` uppercase slate, immediate `display-kpi` numerical value, followed by an inline trend indicator chip (green delta positive, rose delta negative) and baseline volume sparkline.

### Input Fields & Natural Language Bar
- **Query Filter Input:** Height 36px, `#FFFFFF` background with inset `#E2E8F0` border, 4px radius. Left-aligned search icon, right-aligned `[⌘K]` shortcut badge in `JetBrains Mono`.
- **Focus States:** High-visibility ring with 2px offset using `secondary_color_hex` (`#4F46E5`).

### Checkboxes & Toggle Controls
- **Checkboxes:** Crisp 14px x 14px square, 2px border radius, `#CBD5E1` border in unchecked state, `#0F172A` fill with sharp white checkmark when active.