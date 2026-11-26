import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="POV: In Your DM - 장난이라는 이름의 폭력",
    layout="centered",
)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>POV: In Your DM - 장난이라는 이름의 폭력</title>
  <!-- 영문 귀여운 폰트(Quicksand, Nunito) + 손글씨 후보 10종 + 한글 웹폰트(Pretendard, Gmarket Sans) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Dongle:wght@400;700&family=Gaegu:wght@400;700&family=Gamja+Flower&family=Gowun+Batang&family=Gowun+Dodum&family=Hi+Melody&family=Jua&family=Nanum+Pen+Script&family=Nunito:wght@400;500;600&family=Poor+Story&family=Quicksand:wght@500;600&family=Single+Day&display=swap" rel="stylesheet">
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <link href="https://webfontworld.github.io/gmarket/GmarketSans.css" rel="stylesheet" />
  <style>
    :root {
      --bg-main: #FFFDF7;
      --bg-card: #FFFFFF;
      --bg-butter: #FFF6D6;
      --bg-butter-accent: #FBE39D;
      --bg-soft: #FAF7EE;
      --text-primary: #2D2A26;
      --text-secondary: #5C564E;
      --text-muted: #8E8677;
      /* 카카오톡 스타일 파스텔 톤 채팅방 컬러 */
      --kakao-bg: #DCE6F2;
      --kakao-header: #D2DFEE;
      --kakao-my-bubble: #FEE500;
      --kakao-other-bubble: #FFFFFF;
      --kakao-unread: #D98A00;
      --border-light: #EFEAD8;
      --border-butter: #F5D67B;
      --danger: #D94E5C;
      --danger-bg: #FFF3F4;
      --success: #228B5B;
      --success-bg: #EFFAF4;
      --shadow-card: 0 14px 36px rgba(92, 78, 45, 0.08);
      --shadow-float: 0 8px 24px rgba(92, 78, 45, 0.14);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Quicksand', 'Nunito', 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      font-weight: 400;
    }

    body {
      background-color: var(--bg-main);
      color: var(--text-primary);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 16px;
      font-size: 17px;
      line-height: 1.65;
    }

    /* 메인 앱 컨테이너 */
    .app-container {
      width: 100%;
      max-width: 500px;
      background: var(--bg-card);
      border-radius: 30px;
      box-shadow: var(--shadow-card);
      border: 1.5px solid var(--border-light);
      overflow: hidden;
      position: relative;
      min-height: 720px;
      display: flex;
      flex-direction: column;
    }

    /* 상단 진행 바 */
    .top-bar {
      padding: 16px 24px;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-light);
      display: none;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      z-index: 10;
    }

    .step-label {
      font-size: 14px;
      color: var(--text-secondary);
      letter-spacing: 0.04em;
    }

    .progress-track {
      flex: 1;
      height: 8px;
      background: var(--bg-soft);
      border-radius: 999px;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: var(--bg-butter-accent);
      border-radius: 999px;
      transition: width 0.4s ease;
    }

    /* 화면 전환 */
    .screen {
      display: none;
      padding: 32px 26px;
      flex: 1;
      flex-direction: column;
      animation: fadeIn 0.35s ease;
    }

    .screen.active {
      display: flex;
    }

    /* 카톡 채팅방 전용 패딩 초기화 */
    #screenChat {
      padding: 0;
      background: var(--kakao-bg);
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-6px); }
      40%, 80% { transform: translateX(6px); }
    }

    @keyframes notiPop {
      0% { opacity: 0; transform: translateY(-16px) scale(0.95); }
      65% { opacity: 1; transform: translateY(3px) scale(1.01); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .noti-pop-anim {
      animation: notiPop 0.55s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .shake {
      animation: shake 0.35s ease;
    }

    /* 타이틀 및 타이포그래피 */
    .title-display {
      font-family: 'Quicksand', 'GmarketSans', 'Pretendard', sans-serif;
      font-weight: 600;
      font-size: 33px;
      line-height: 1.3;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }

    .subtitle-display {
      font-size: 20px;
      color: var(--text-secondary);
      margin-top: 8px;
      line-height: 1.5;
    }

    /* 1. 시작 화면 */
    .intro-hero {
      margin-top: 24px;
      margin-bottom: 32px;
      text-align: center;
    }

    /* 교사용 은은한 비밀 진입 아이콘 (첫 화면 우측 상단) */
    .secret-teacher-btn {
      position: absolute;
      top: 14px;
      right: 16px;
      width: 30px;
      height: 30px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-size: 13px;
      opacity: 0.25;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      transition: opacity 0.2s ease, background 0.2s ease;
      z-index: 5;
    }

    .secret-teacher-btn:hover {
      opacity: 0.65;
      background: var(--bg-soft);
    }

    .tutor-intro-card {
      background: var(--bg-butter);
      border: 1.5px solid var(--border-butter);
      border-radius: 22px;
      padding: 20px 22px;
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 32px;
    }

    .tutor-emoji-badge {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 1.5px solid var(--border-butter);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 30px;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(180, 145, 50, 0.12);
    }

    .tutor-intro-text {
      font-size: 16px;
      color: var(--text-primary);
      line-height: 1.6;
    }

    .input-group {
      margin-bottom: 24px;
    }

    .input-label {
      display: block;
      font-size: 16px;
      color: var(--text-primary);
      margin-bottom: 10px;
    }

    .text-input {
      width: 100%;
      padding: 16px 18px;
      font-size: 18px;
      border: 1.5px solid var(--border-light);
      border-radius: 16px;
      background: #FFFFFF;
      color: var(--text-primary);
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .text-input:focus {
      border-color: var(--border-butter);
      box-shadow: 0 0 0 4px rgba(251, 227, 157, 0.35);
    }

    .error-msg {
      color: var(--danger);
      font-size: 15px;
      margin-top: 8px;
      min-height: 22px;
    }

    /* 버튼 공통 */
    .btn-primary {
      width: 100%;
      padding: 18px 24px;
      font-size: 18px;
      background: var(--bg-butter-accent);
      color: var(--text-primary);
      border: 1.5px solid var(--border-butter);
      border-radius: 18px;
      cursor: pointer;
      transition: background 0.2s ease, transform 0.1s ease;
      margin-top: auto;
    }

    .btn-primary:hover {
      background: #F9D97A;
    }

    .btn-primary:active {
      transform: scale(0.99);
    }

    .btn-secondary {
      width: 100%;
      padding: 15px 20px;
      font-size: 16px;
      background: var(--bg-soft);
      color: var(--text-primary);
      border: 1.5px solid var(--border-light);
      border-radius: 16px;
      cursor: pointer;
      transition: background 0.2s ease;
    }

    .btn-secondary:hover {
      background: var(--bg-butter);
    }

    /* 2. SCENARIO 화면 */
    .scenario-badge {
      display: inline-block;
      padding: 6px 14px;
      background: var(--bg-butter);
      border: 1px solid var(--border-butter);
      color: var(--text-primary);
      border-radius: 999px;
      font-size: 14px;
      letter-spacing: 0.08em;
      margin-bottom: 16px;
      align-self: flex-start;
    }

    .phone-notification {
      background: #FFFFFF;
      border: 1.5px solid var(--border-butter);
      border-radius: 22px;
      padding: 18px 20px;
      margin: 18px 0 22px;
      box-shadow: 0 10px 26px rgba(92, 78, 45, 0.12);
    }

    .noti-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13.5px;
      color: var(--text-muted);
      margin-bottom: 8px;
    }

    .noti-app-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #FEE500;
      color: #2D2A26;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 500;
    }

    .noti-body {
      font-size: 16.5px;
      color: var(--text-primary);
      line-height: 1.6;
    }

    .learning-takeaway-box {
      background: #FFFFFF;
      border: 1.5px solid var(--border-butter);
      border-radius: 18px;
      padding: 16px 18px;
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .takeaway-item {
      font-size: 15.5px;
      color: var(--text-primary);
      line-height: 1.6;
    }

    .takeaway-badge {
      display: inline-block;
      background: var(--bg-butter);
      border: 1px solid var(--border-butter);
      border-radius: 999px;
      padding: 2px 10px;
      font-size: 13px;
      margin-bottom: 4px;
      color: var(--text-primary);
    }

    /* 핵심 이론 텍스트 연노랑 형광펜 스타일 */
    .theory-text-underline {
      background: linear-gradient(180deg, transparent 54%, #FFF3B8 54%, #FFF3B8 90%, transparent 90%);
      padding: 1px 4px;
      border-radius: 4px;
      box-decoration-break: clone;
      -webkit-box-decoration-break: clone;
      color: var(--text-primary);
    }

    .scenario-desc {
      font-size: 17px;
      color: var(--text-secondary);
      line-height: 1.75;
      margin-bottom: 24px;
    }

    /* 3. 실제 카카오톡 스타일 메신저 화면 */
    .kakao-header {
      background: var(--kakao-header);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    }

    .kakao-header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .kakao-back-icon {
      font-size: 20px;
      color: #2B333E;
      line-height: 1;
    }

    .kakao-room-title {
      font-size: 18px;
      font-weight: 500;
      color: #1E242B;
    }

    .kakao-room-sub {
      font-size: 12.5px;
      color: #536273;
    }

    .kakao-header-icons {
      display: flex;
      gap: 12px;
      font-size: 17px;
      color: #2B333E;
    }

    .chat-area {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 14px;
      padding: 16px 16px 12px;
      overflow-y: auto;
      max-height: 310px;
    }

    .kakao-date-pill {
      align-self: center;
      background: rgba(65, 82, 102, 0.18);
      color: #FFFFFF;
      font-size: 12.5px;
      padding: 4px 14px;
      border-radius: 999px;
      margin-bottom: 4px;
    }

    .typing-indicator {
      align-self: flex-start;
      background: rgba(255, 255, 255, 0.85);
      padding: 10px 16px;
      border-radius: 18px;
      font-size: 14px;
      color: #5A6777;
      display: none;
    }

    /* 상대방(민수) 카톡 메시지 행 */
    .kakao-msg-row.other {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      animation: fadeIn 0.3s ease;
    }

    .kakao-profile-pic {
      width: 40px;
      height: 40px;
      border-radius: 15px;
      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
    }

    .kakao-msg-col {
      display: flex;
      flex-direction: column;
      max-width: 82%;
    }

    .kakao-sender-name {
      font-size: 13px;
      color: #3D4A59;
      margin-bottom: 4px;
      margin-left: 2px;
    }

    .kakao-bubble-line {
      display: flex;
      align-items: flex-end;
      gap: 6px;
    }

    .kakao-bubble.other {
      position: relative;
      background: var(--kakao-other-bubble);
      color: #1E2024;
      padding: 12px 15px;
      border-radius: 16px;
      border-top-left-radius: 4px;
      font-family: 'Nunito', 'Quicksand', 'Pretendard', sans-serif;
      font-weight: 500;
      font-size: 16.5px;
      line-height: 1.55;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06);
    }

    /* 내 카톡 메시지 행 */
    .kakao-msg-row.me {
      display: flex;
      justify-content: flex-end;
      align-items: flex-end;
      gap: 6px;
      animation: fadeIn 0.3s ease;
    }

    .kakao-bubble.me {
      max-width: 78%;
      background: var(--kakao-my-bubble);
      color: #1E2024;
      padding: 12px 15px;
      border-radius: 16px;
      border-top-right-radius: 4px;
      font-family: 'Nunito', 'Quicksand', 'Pretendard', sans-serif;
      font-weight: 500;
      font-size: 16.5px;
      line-height: 1.55;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06);
    }

    .kakao-meta-col {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      flex-shrink: 0;
      line-height: 1.2;
    }

    .kakao-msg-row.me .kakao-meta-col {
      align-items: flex-end;
    }

    .kakao-unread {
      font-size: 11.5px;
      font-weight: 600;
      color: var(--kakao-unread);
      margin-bottom: 2px;
    }

    .kakao-time {
      font-size: 11px;
      color: #556475;
      white-space: nowrap;
    }

    .translate-btn {
      align-self: flex-start;
      margin-top: 7px;
      background: rgba(255, 255, 255, 0.85);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 999px;
      padding: 4px 12px;
      font-size: 13px;
      color: #3D4A59;
      cursor: pointer;
      transition: background 0.2s;
    }

    .translate-btn:hover {
      background: #FFFFFF;
    }

    .translated-text {
      display: none;
      margin-top: 6px;
      padding: 10px 14px;
      background: rgba(255, 255, 255, 0.92);
      border-left: 3px solid #FEE500;
      border-radius: 10px;
      font-size: 15px;
      color: var(--text-primary);
      line-height: 1.55;
    }

    /* 카톡 하단 짝꿍 미션 패널 */
    .mission-box {
      background: #FFFFFF;
      border-top: 1px solid var(--border-light);
      border-radius: 24px 24px 0 0;
      padding: 20px 22px 24px;
      margin-top: auto;
      box-shadow: 0 -6px 20px rgba(0, 0, 0, 0.04);
    }

    .mission-title {
      font-size: 16.5px;
      color: var(--text-primary);
      margin-bottom: 12px;
      line-height: 1.5;
    }

    .option-list {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      padding: 13px 16px;
      font-size: 15.5px;
      line-height: 1.5;
      background: var(--bg-soft);
      color: var(--text-primary);
      border: 1.5px solid var(--border-light);
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .option-btn:hover {
      border-color: var(--border-butter);
      background: var(--bg-butter);
    }

    .option-btn.wrong {
      border-color: var(--danger);
      background: var(--danger-bg);
      color: var(--danger);
    }

    .option-btn.correct {
      border-color: var(--success);
      background: var(--success-bg);
      color: var(--success);
    }

    .feedback-banner {
      margin-top: 10px;
      font-size: 14.5px;
      min-height: 20px;
      color: var(--danger);
    }

    .feedback-banner.success {
      color: var(--success);
    }

    /* 4. 핵심 정리 퀴즈 */
    .quiz-badge {
      display: inline-block;
      padding: 6px 14px;
      background: var(--bg-butter);
      border: 1px solid var(--border-butter);
      color: var(--text-primary);
      border-radius: 999px;
      font-size: 14px;
      margin-bottom: 16px;
      align-self: flex-start;
    }

    .quiz-question {
      font-size: 19px;
      color: var(--text-primary);
      line-height: 1.65;
      margin-bottom: 22px;
    }

    .chosung-box {
      background: var(--bg-butter);
      border: 1.5px solid var(--border-butter);
      border-radius: 18px;
      padding: 22px;
      text-align: center;
      font-size: 28px;
      letter-spacing: 0.2em;
      color: var(--text-primary);
      margin-bottom: 20px;
    }

    .ox-group {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    .ox-btn {
      padding: 26px;
      font-size: 28px;
      background: #FFFFFF;
      border: 1.5px solid var(--border-light);
      border-radius: 18px;
      cursor: pointer;
      color: var(--text-primary);
      transition: all 0.2s;
    }

    .ox-btn:hover {
      border-color: var(--border-butter);
      background: var(--bg-butter);
    }

    /* 5. 소감 작성 화면 */
    .ending-card {
      background: var(--bg-butter);
      border: 1.5px solid var(--border-butter);
      border-radius: 22px;
      padding: 22px;
      margin: 16px 0;
    }

    .ending-quote {
      font-family: 'Quicksand', 'Nunito', 'Pretendard', sans-serif;
      font-weight: 600;
      font-size: 20px;
      color: var(--text-primary);
      line-height: 1.6;
      margin-bottom: 8px;
    }

    .ending-sub {
      font-size: 16px;
      color: var(--text-secondary);
      line-height: 1.65;
    }

    textarea.reflection-input {
      width: 100%;
      min-height: 115px;
      padding: 16px;
      font-size: 16px;
      line-height: 1.6;
      border: 1.5px solid var(--border-light);
      border-radius: 16px;
      resize: vertical;
      outline: none;
      margin-bottom: 8px;
    }

    textarea.reflection-input:focus {
      border-color: var(--border-butter);
      box-shadow: 0 0 0 4px rgba(251, 227, 157, 0.35);
    }

    .btn-row {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 8px;
    }

    /* 6. MISSION CLEAR! 축하 화면 */
    #screenMissionClear {
      position: relative;
      overflow: hidden;
      text-align: center;
      justify-content: center;
      align-items: center;
    }

    .confetti-layer {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
    }

    .confetti-piece {
      position: absolute;
      top: -20px;
      width: 10px;
      height: 14px;
      border-radius: 3px;
      opacity: 0.9;
      animation: confettiFall linear forwards;
    }

    @keyframes confettiFall {
      0% {
        transform: translateY(-20px) rotate(0deg);
        opacity: 1;
      }
      100% {
        transform: translateY(740px) rotate(540deg);
        opacity: 0;
      }
    }

    .clear-trophy-wrap {
      position: relative;
      width: 108px;
      height: 108px;
      border-radius: 50%;
      background: var(--bg-butter);
      border: 2px solid var(--border-butter);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 54px;
      margin-bottom: 20px;
      box-shadow: 0 10px 24px rgba(245, 214, 123, 0.45);
      animation: popBounce 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    @keyframes popBounce {
      0% { transform: scale(0.4); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    .clear-badge {
      display: inline-block;
      padding: 6px 16px;
      background: var(--bg-butter);
      border: 1.5px solid var(--border-butter);
      border-radius: 999px;
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      font-size: 15px;
      letter-spacing: 0.1em;
      color: var(--text-primary);
      margin-bottom: 12px;
    }

    .clear-title {
      font-family: 'Quicksand', 'GmarketSans', sans-serif;
      font-weight: 600;
      font-size: 36px;
      color: var(--text-primary);
      margin-bottom: 12px;
      letter-spacing: 0.02em;
    }

    .clear-message-card {
      background: var(--bg-soft);
      border: 1.5px solid var(--border-light);
      border-radius: 22px;
      padding: 22px;
      margin: 16px 0 26px;
      width: 100%;
    }

    .clear-main-msg {
      font-family: 'Hi Melody', 'Pretendard', sans-serif;
      font-weight: 400;
      font-size: 20px;
      color: var(--text-primary);
      line-height: 1.45;
      margin-bottom: 0;
    }

    /* 우측 하단 토끼선생님(🐰) 플로팅 튜터 */
    .tutor-floating-wrap {
      position: fixed;
      bottom: 24px;
      right: 24px;
      display: none;
      flex-direction: column;
      align-items: flex-end;
      gap: 12px;
      z-index: 100;
      max-width: 330px;
    }

    .tutor-bubble {
      background: #FFFFFF;
      border: 1.5px solid var(--border-butter);
      border-radius: 22px;
      padding: 18px 20px;
      box-shadow: var(--shadow-float);
      font-size: 15px;
      line-height: 1.65;
      color: var(--text-primary);
      display: block;
    }

    .tutor-bubble-header {
      font-size: 14px;
      color: var(--text-secondary);
      background: var(--bg-butter);
      display: inline-block;
      padding: 2px 10px;
      border-radius: 999px;
      margin-bottom: 8px;
    }

    .tutor-toggle-btn {
      width: 62px;
      height: 62px;
      border-radius: 50%;
      background: var(--bg-butter);
      border: 2px solid var(--border-butter);
      box-shadow: var(--shadow-float);
      font-size: 32px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s ease;
    }

    .tutor-toggle-btn:hover {
      transform: scale(1.07);
    }

    /* 모달: 참여자 소감 모아보기 */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(38, 35, 29, 0.45);
      display: none;
      justify-content: center;
      align-items: center;
      padding: 20px;
      z-index: 200;
    }

    .modal-card {
      background: #FFFFFF;
      width: 100%;
      max-width: 500px;
      max-height: 82vh;
      border-radius: 26px;
      padding: 28px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-float);
      border: 1.5px solid var(--border-light);
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-light);
    }

    .modal-title {
      font-size: 20px;
      color: var(--text-primary);
    }

    .close-btn {
      background: none;
      border: none;
      font-size: 26px;
      color: var(--text-muted);
      cursor: pointer;
    }

    .reflection-list {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 18px;
      padding-right: 4px;
    }

    .reflection-item {
      background: var(--bg-soft);
      padding: 16px;
      border-radius: 16px;
    }

    .reflection-meta {
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    .reflection-text {
      font-size: 16px;
      color: var(--text-primary);
      line-height: 1.6;
    }

    /* 교사 비밀번호 잠금 영역 */
    .teacher-lock-box {
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 12px 0 8px;
    }

    .teacher-lock-desc {
      font-size: 15.5px;
      color: var(--text-secondary);
      line-height: 1.6;
    }
  </style>
</head>
<body>

  <div class="app-container">
    <!-- 상단 진행바 -->
    <div class="top-bar" id="topBar" style="display: none;">
      <span class="step-label" id="stepLabel">SCENARIO 1</span>
      <div class="progress-track">
        <div class="progress-fill" id="progressFill"></div>
      </div>
    </div>

    <!-- 1. 시작 화면 -->
    <section class="screen active" id="screenIntro">
      <button
        type="button"
        class="secret-teacher-btn"
        id="secretTeacherBtn"
        title="교사 소감 확인"
        aria-label="참여자 소감 모아보기"
      >🔑</button>

      <div class="intro-hero">
        <h1 class="title-display">POV: In Your DM</h1>
        <p class="subtitle-display">장난이라는 이름의 폭력</p>
      </div>

      <div class="tutor-intro-card">
        <div class="tutor-emoji-badge">🐰</div>
        <div class="tutor-intro-text">
          안녕! 나는 너의 활동을 도와줄 토끼선생님이야.<br />
          옆자리 짝꿍과 함께 대화 속에 숨겨진 진짜 의도를 찾아보자!
        </div>
      </div>

      <div class="input-group">
        <label class="input-label" for="studentNameInput">참여자 이름</label>
        <input
          type="text"
          id="studentNameInput"
          class="text-input"
          placeholder="이름을 입력해 주세요"
          autocomplete="off"
        />
        <div class="error-msg" id="nameErrorMsg"></div>
      </div>

      <button type="button" class="btn-primary" id="startBtn">활동 시작하기</button>
    </section>

    <!-- 2. SCENARIO 도입 화면 (Stage 1 & Stage 2 전환 공용) -->
    <section class="screen" id="screenScenario">
      <span class="scenario-badge" id="scenarioBadge">SCENARIO 1</span>
      <h2 class="title-display" id="scenarioTitle" style="font-size: 26px;">밤 10시 30분, 단톡방 강퇴와 개인 톡</h2>

      <div class="phone-notification" id="scenarioNotiBox">
        <div class="noti-header">
          <span class="noti-app-tag">💬 카카오톡 알림</span>
          <span id="scenarioNotiTime">오후 10:30</span>
        </div>
        <div class="noti-body" id="scenarioNotiBody">
          [2학년 3반 단톡방] 민수님이 <span class="user-name-slot">학생</span>님을 내보냈습니다.<br />
          민수님으로부터 개인 메시지 1건이 도착했습니다.
        </div>
      </div>

      <p class="scenario-desc" id="scenarioDesc">
        새 학기가 시작된 뒤 반 안에 명확한 배려의 기준이 자리 잡지 못한 틈을 타, 민수와 몇몇 친구들은 누군가를 공개적으로 깎아내리고 공격하는 행동을 놀이처럼 주고받기 시작했습니다.<br /><br />
        오늘 점심시간 급식실에서의 의도적인 자리 피하기와 체육 시간의 귓속말에 이어, 밤 10시 30분 반 단톡방에서 <span class="user-name-slot">학생</span>님을 강제로 내보낸 직후 민수에게서 조롱과 비하가 담긴 개인 톡이 날아옵니다. 옆자리 짝꿍과 함께 메시지 속 숨은 의도를 파악해 주세요.
      </p>

      <button type="button" class="btn-primary" id="goStageBtn">카톡 확인하기</button>
    </section>

    <!-- 3. 실제 카카오톡 스타일 DM 시뮬레이션 (Stage 1 & Stage 2) -->
    <section class="screen" id="screenChat">
      <div class="kakao-header">
        <div class="kakao-header-left">
          <span class="kakao-back-icon">‹</span>
          <div>
            <div class="kakao-room-title" id="chatPartnerName">민수</div>
            <div class="kakao-room-sub" id="chatStageSubtitle">Stage 1 · 개인 톡</div>
          </div>
        </div>
        <div class="kakao-header-icons">
          <span>🔍</span>
          <span>☰</span>
        </div>
      </div>

      <div class="chat-area" id="chatArea">
        <div class="typing-indicator" id="typingIndicator">상대방이 입력 중입니다...</div>
      </div>

      <div class="mission-box" id="missionBox" style="display: none;">
        <div class="mission-title" id="missionTitle"></div>
        <div class="option-list" id="optionList"></div>
        <div class="feedback-banner" id="missionFeedback"></div>
      </div>
    </section>

    <!-- 3-1. Stage 클리어 후 학습 정리(Aftermath) 화면 -->
    <section class="screen" id="screenStageResult">
      <span class="scenario-badge" id="stageResultBadge">STAGE 1 CLEAR</span>
      <h2 class="title-display" id="stageResultTitle" style="font-size: 25px;">Stage 1에서 배운 핵심 포인트</h2>

      <div class="ending-card" style="margin: 18px 0;">
        <p class="ending-quote" id="stageResultSubtitle" style="font-size: 17.5px; margin-bottom: 8px;"></p>
        <p class="ending-sub" id="stageResultDesc" style="font-size: 15.5px;"></p>

        <div class="learning-takeaway-box">
          <div class="takeaway-item">
            <span class="takeaway-badge">🗣️ 핵심 영어 대항 담화 표현</span>
            <div id="stageResultEnglish"></div>
          </div>
          <div class="takeaway-item">
            <span class="takeaway-badge">📚 학교폭력 이론 연결하기</span>
            <div id="stageResultTheory"></div>
          </div>
        </div>
      </div>

      <button type="button" class="btn-primary" id="stageResultNextBtn">다음 단계로 이동하기</button>
    </section>

    <!-- 4. 핵심 정리 퀴즈 (5문제) -->
    <section class="screen" id="screenQuiz">
      <span class="quiz-badge" id="quizCounter">핵심 정리 퀴즈 1 / 5</span>
      <div class="quiz-question" id="quizQuestion"></div>

      <!-- 초성 / 단답형 퀴즈 -->
      <div id="quizChosungWrap" style="display: none;">
        <div class="chosung-box" id="quizChosungDisplay"></div>
        <input
          type="text"
          id="quizTextInput"
          class="text-input"
          placeholder="정답을 입력하세요"
          autocomplete="off"
        />
        <button type="button" class="btn-primary" id="quizTextSubmitBtn" style="margin-top: 16px;">정답 확인하기</button>
      </div>

      <!-- 객관식 -->
      <div class="option-list" id="quizOptionList" style="display: none;"></div>

      <!-- O/X -->
      <div class="ox-group" id="quizOxWrap" style="display: none;">
        <button type="button" class="ox-btn" data-ox="O">O</button>
        <button type="button" class="ox-btn" data-ox="X">X</button>
      </div>

      <div class="feedback-banner" id="quizFeedback" style="margin-top: 16px;"></div>
    </section>

    <!-- 5. 소감 작성 화면 -->
    <section class="screen" id="screenEnding">
      <span class="scenario-badge">REFLECTION</span>
      <h2 class="title-display" style="font-size: 26px;">오늘의 활동을 마무리하며</h2>

      <div class="ending-card">
        <p class="ending-quote">“It was never your fault, <span class="user-name-slot">학생</span>.”</p>
        <p class="ending-sub">
          장난이라는 말로 포장해도 상처가 된다면 분명한 폭력입니다. 혼자 고민하지 않고 짝꿍과 함께 대응한 것처럼, 우리 반의 든든한 방어자가 되어주세요.
        </p>
      </div>

      <div class="input-group" style="margin-bottom: 12px;">
        <label class="input-label" for="reflectionInput">오늘 활동 소감을 자유롭게 적어주세요</label>
        <textarea
          id="reflectionInput"
          class="reflection-input"
          placeholder="예: 장난처럼 던지는 말도 상대방에게는 큰 상처가 될 수 있다는 걸 느꼈어요."
        ></textarea>
        <div class="feedback-banner" id="reflectionFeedback"></div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-primary" id="saveReflectionBtn">활동 소감 제출하기</button>
      </div>
    </section>

    <!-- 6. MISSION CLEAR! 축하 화면 -->
    <section class="screen" id="screenMissionClear">
      <div class="confetti-layer" id="confettiLayer"></div>

      <div class="clear-trophy-wrap">🎉</div>
      <span class="clear-badge">ALL STAGES COMPLETED</span>
      <h2 class="clear-title">MISSION CLEAR!</h2>

      <div class="clear-message-card">
        <p class="clear-main-msg" id="clearMainMsg">
          학교폭력예방및학생의이해 남은 수업도<br />
          파이팅합시다! 잘 참여해주셔서 감사합니다 ദ്ദി･ω･`)
        </p>
      </div>
    </section>
  </div>

  <!-- 우측 하단 토끼선생님(🐰) 플로팅 튜터 -->
  <div class="tutor-floating-wrap" id="tutorFloatingWrap">
    <div class="tutor-bubble" id="tutorBubble">
      <div class="tutor-bubble-header">🐰 토끼선생님</div>
      <div id="tutorHintText">모르는 점이 있다면 토끼선생님을 눌러서 힌트를 받아보세요!</div>
    </div>
    <button type="button" class="tutor-toggle-btn" id="tutorToggleBtn" title="토끼선생님 힌트 열기/닫기">🐰</button>
  </div>

  <!-- 참여자 소감 모아보기 모달 -->
  <div class="modal-overlay" id="reflectionModal">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">참여자 활동 소감 모음</h3>
        <button type="button" class="close-btn" id="closeModalBtn">&times;</button>
      </div>

      <!-- 교사 비밀번호 인증 화면 -->
      <div class="teacher-lock-box" id="teacherLockBox">
        <p class="teacher-lock-desc">
          참여자 활동 소감은 교사 확인용입니다.<br />
          교사 비밀번호를 입력해 주세요.
        </p>
        <input
          type="password"
          id="teacherPasswordInput"
          class="text-input"
          placeholder="교사 비밀번호 입력"
          autocomplete="off"
        />
        <div class="error-msg" id="teacherAuthError"></div>
        <button type="button" class="btn-primary" id="teacherUnlockBtn">확인하고 소감 보기</button>
      </div>

      <!-- 인증 완료 후 소감 목록 영역 -->
      <div id="teacherUnlockedContent" style="display: none; flex: 1; flex-direction: column; min-height: 0;">
        <div class="reflection-list" id="reflectionListContainer"></div>
        <button type="button" class="btn-primary" id="copyReflectionsBtn">전체 소감 복사하기</button>
      </div>
    </div>
  </div>

  <script>
    // 전역 상태
    let studentName = "";
    let currentScenarioNum = 1;
    let currentStepIndex = 0;
    let currentQuizIndex = 0;
    let isTutorBubbleVisible = true;
    let currentHintContent = "";
    let hasClickedTutorInStep = false;
    let memoryReflections = [];

    const scenarios = {
      1: {
        badge: "SCENARIO 1",
        title: "밤 10시 30분, 단톡방 강퇴와 공격적인 개인 톡",
        notiTime: "오후 10:30",
        notiBody: "[2학년 3반 단톡방] 민수님이 {name}님을 내보냈습니다.<br />민수님으로부터 개인 메시지 1건이 도착했습니다.",
        desc: "새 학기가 시작된 뒤 반 안에 명확한 배려의 기준이 자리 잡지 못한 틈을 타, 민수와 몇몇 친구들은 누군가를 공개적으로 깎아내리고 공격하는 행동을 놀이처럼 주고받기 시작했습니다.<br /><br />오늘 점심시간 급식실에서의 의도적인 자리 피하기와 체육 시간의 귓속말에 이어, 밤 10시 30분 반 단톡방에서 {name}님을 강제로 내보낸 직후 민수에게서 조롱과 비하가 담긴 개인 톡이 날아옵니다. 옆자리 짝꿍과 함께 메시지 속 숨은 의도를 파악해 주세요.",
        partnerName: "민수",
        partnerEmoji: "🧑🏻",
        datePill: "어젯밤",
        btnText: "Stage 1 카톡 확인하기",
        resultBadge: "STAGE 1 LEARNING POINT",
        resultTitle: "Stage 1에서 배운 핵심 정리",
        resultSubtitle: "사이버 언어폭력과 소외에 단호하게 선을 그었어요!",
        resultDesc: "위축되지 않고 단호하게 거부 의사를 밝히자 민수는 더 이상 비하하는 말을 이어가지 못했습니다. 이번 대화에 담긴 사이버폭력 유형과 이론을 확인해 보세요.",
        resultEnglish: "<strong>“Stop talking to me like that. I won't put up with your insults.”</strong><br />상대의 비하와 모욕에 사과하며 주눅 들지 않고, 공격적인 언행을 즉각 중단하라고 요구하는 대항 담화(Counter-discourse) 표현입니다.",
        resultTheory: "<span class=\"theory-text-underline\">사이버 언어폭력·소외 &amp; 낙인이론(Labeling Theory)</span><br />• <strong>사이버 언어폭력·소외:</strong> 단톡방에서 강제로 내보내 집단에서 배제(소외)하고, 개인 메신저로 외모나 행동을 비하·모욕하는 언사를 보내 심리적 고통을 주는 사이버폭력입니다.<br />• <strong>낙인이론(Labeling Theory):</strong> 가해자가 <em>“눈치도 없고 분위기 망치는 애”</em>라는 부정적 꼬리표를 씌워 집단 안에서 고립시키고 그 역할에 가두려는 현상입니다.",
        resultBtnText: "다음 날 상황(Stage 2) 보기",
        steps: [
          {
            stageLabel: "Stage 1 · 사이버 언어폭력·소외와 낙인찍기",
            progress: 22,
            isNewMessage: true,
            timeLabel: "오후 10:31",
            enText: "OMG, {name}, why do you even bother posting selfies or talking in the group chat? Honestly, nobody wants to see your face—you're just embarrassing yourself and ruining the vibe! 😂",
            koText: "헐 {name}아, 넌 대체 왜 셀카를 올리고 단톡방에서 말까지 걸어? 솔직히 아무도 네 얼굴 보고 싶어 하지 않아—네 스스로 망신당하면서 분위기만 망치고 있잖아! 😂",
            hint: "단톡방 강퇴(소외)에 이어 개인 톡으로 외모와 행동을 직접 모욕(사이버 언어폭력)하면서, '분위기를 망치는 눈치 없는 애'라는 부정적 낙인을 찍는 메시지야!",
            missionTitle: "[짝꿍 미션 1] 가해자가 이 메시지를 보낸 진짜 의도는 무엇일까요?",
            options: [
              "단톡방의 어색한 분위기를 풀어주기 위해 유쾌하게 농담을 건네는 것",
              "친구의 SNS 게시물이 더 많은 관심을 받을 수 있도록 진심으로 조언하려는 것",
              "모욕적인 언어폭력으로 상대를 위축시키고, 집단 분위기를 망치는 존재라는 부정적 낙인을 찍어 고립시키려는 것"
            ],
            answerIndex: 2
          },
          {
            stageLabel: "Stage 1 · 화용적 대항 담화 선택",
            progress: 38,
            isNewMessage: false,
            timeLabel: "오후 10:32",
            hint: "상대의 모욕과 비하(사이버 언어폭력)에 말려들어 사과하거나 같이 욕설로 맞서지 말고, 무례한 언행을 멈추라고 단호하게 선을 긋는 답장을 골라보자!",
            missionTitle: "[짝꿍 미션 2] 가해자의 언어폭력과 낙인찍기를 끊어내는 가장 적절한 답장은?",
            options: [
              "Stop talking to me like that. I won't put up with your insults. (그런 식으로 말하지 마. 네 모욕적인 말은 참지 않을 거야.)",
              "Sorry... I didn't know everyone felt that way. I'll delete everything. (미안해... 다들 그렇게 생각하는 줄 몰랐어. 다 지울게.)",
              "Haha thanks for letting me know! (하하 알려줘서 고마워!)"
            ],
            answerIndex: 0,
            replyEn: "Stop talking to me like that. I won't put up with your insults."
          }
        ]
      },
      2: {
        badge: "SCENARIO 2",
        title: "다음 날 쉬는 시간, '장난'이라는 이름의 압박",
        notiTime: "오전 10:40",
        notiBody: "[2학년 3반] 지수님으로부터 개인 메시지 1건이 도착했습니다.<br />“야 너 어제 민수한테 정색했다며? 분위기 싸해졌잖아”",
        desc: "다음 날 등교하자마자 민수 무리인 지수에게서 개인 톡이 날아왔습니다. 지수는 어젯밤 일을 두고 '우리끼리는 원래 다 그렇게 밈처럼 놀면서 친해진다'며, 오히려 정색한 {name}님 때문에 반 분위기가 망가졌다고 몰아갑니다.<br /><br />집단의 잘못된 또래 규범을 내세워 피해자를 예민한 사람으로 만드는 상황에서, 짝꿍과 함께 지수의 논리를 반박해 보세요.",
        partnerName: "지수",
        partnerEmoji: "👧🏻",
        datePill: "오늘 쉬는 시간",
        btnText: "Stage 2 카톡 확인하기",
        resultBadge: "STAGE 2 LEARNING POINT",
        resultTitle: "Stage 2에서 배운 핵심 정리",
        resultSubtitle: "'그냥 장난이었다'는 변명을 논리적으로 반박했어요!",
        resultDesc: "다수가 웃는다는 이유로 폭력이 정당화될 수 없음을 분명히 짚어주었습니다. 이번 대화에 담긴 영어 표현과 이론을 정리해 봅시다.",
        resultEnglish: "<strong>“A joke is only funny when everyone laughs. Stop crossing the line.”</strong><br />‘농담은 모두가 웃을 때만 농담’이라는 기준을 제시해 가해자의 합리화를 깨뜨리고 경계를 설정하는 핵심 표현입니다.",
        resultTheory: "<span class=\"theory-text-underline\">차별적 교제 이론 &amp; 중화기술</span><br />• <strong>차별적 교제 이론(Differential Association):</strong> <em>“나랑 애들은 맨날 이런 밈 주고받아”</em>처럼 또래 집단 안에서 조롱과 비하를 일상적 유머로 학습하고 정상화하는 집단 역동입니다.<br />• <strong>중화기술(Neutralization):</strong> <em>“그냥 재밌자고 하는 건데 네가 너무 예민해”</em>라며 가해 행위를 장난으로 축소(가해 부정)하고 피해자 탓으로 돌리는(피해자 비난) 책임 회피 전략입니다.",
        resultBtnText: "핵심 정리 퀴즈 풀기",
        steps: [
          {
            stageLabel: "Stage 2 · 집단 동조와 책임 전가",
            progress: 55,
            isNewMessage: true,
            timeLabel: "오전 10:41",
            enText: "Chill out, {name}. Me and the guys share memes like this all the time—everyone knows it's just for fun. You're the only one taking it seriously and being way too sensitive.",
            koText: "진정해, {name}아. 나랑 애들은 맨날 이런 밈(장난) 주고받아. 다들 그냥 재밌자고 하는 거 아는데 너만 혼자 심각하게 받아들이고 너무 예민하게 구네.",
            hint: "'우리끼리는 원래 이렇게 놀아'라며 괴롭힘을 또래 문화인 것처럼 정당화하고, 상처받은 너를 오히려 '예민한 사람'으로 몰아 책임을 떠넘기고 있어!",
            missionTitle: "[짝꿍 미션 1] 이 메시지에서 가해자가 자신의 행동을 합리화하는 방식은 무엇일까요?",
            options: [
              "자신의 말이 과했다는 것을 인정하고 친구들과 함께 사과하려는 태도",
              "친구들끼리의 일상적인 장난으로 포장해 잘못을 축소하고, 오히려 피해자가 예민하다며 책임을 전가하는 것",
              "온라인 밈 문화를 친절하게 설명해 주며 오해를 풀려는 배려"
            ],
            answerIndex: 1
          },
          {
            stageLabel: "Stage 2 · 화용적 대항 담화 선택",
            progress: 70,
            isNewMessage: false,
            timeLabel: "오전 10:42",
            hint: "'다들 그렇게 논다'거나 '장난이다'라는 변명이 통하지 않도록, 당사자가 불쾌하다면 폭력이라는 기준을 분명히 세워주자!",
            missionTitle: "[짝꿍 미션 2] '원래 다 장난으로 하는 거야'라는 합리화를 무력화하는 최선의 대응은?",
            options: [
              "Oh, I see. I guess I overreacted. (아 그렇구나. 내가 너무 과민반응했나 봐.)",
              "Whatever, do whatever you want. (됐어, 너희 마음대로 해.)",
              "Just because you guys call it a joke doesn't make it okay. A joke is only funny when everyone laughs—stop crossing the line. (너희끼리 장난이라고 부른다고 괜찮아지는 건 아니야. 농담은 모두가 웃을 때만 재밌는 거야. 선 넘지 마.)"
            ],
            answerIndex: 2,
            replyEn: "Just because you guys call it a joke doesn't make it okay. A joke is only funny when everyone laughs—stop crossing the line."
          }
        ]
      }
    };

    const quizData = [
      {
        type: "chosung",
        question: "1. 국가 수준의 학교폭력 예방 교육 프로그램으로, 온·오프라인상의 학교폭력 위험으로부터 자신과 친구들을 적극적으로 방어하는 역량을 기르는 이 프로그램의 이름은 무엇일까요?",
        chosung: "ㅇㅇㄹ ㅍㄹㄱㄹ",
        answers: ["어울림 프로그램", "어울림프로그램"],
        hint: "학생들이 서로 조화롭게 어우러진다는 의미를 담은 7글자(띄어쓰기 제외 6글자) 프로그램 이름이야!"
      },
      {
        type: "choice",
        question: "2. 다음 중 어울림 프로그램의 목적으로 올바른 것은?",
        options: [
          "학교폭력 사안 발생 시 가해 학생에 대한 징계 수위와 처벌 절차를 규정하기 위함이다.",
          "학생들이 삶 속에서 다른 친구들을 배려·공감하고 자신의 감정을 이해·조절하며, 갈등을 대화로 해결하고 학교폭력에 지혜롭게 대처할 수 있도록 한다.",
          "단기간의 일회성 특강을 통해 모든 학생에게 동일한 암기식 규칙을 전달하기 위함이다."
        ],
        answerIndex: 1,
        hint: "배려와 공감, 감정 조절, 대화 해결을 통해 학교폭력에 지혜롭게 대처하도록 돕는 것이 어울림 프로그램의 핵심 목적이야!"
      },
      {
        type: "choice",
        question: "3. 교사가 교육과정을 재구성하고 학생의 발달 단계와 학급 특성에 따라 필요한 부분을 선택하여 활용할 수 있도록 개발된 어울림 프로그램의 구성 형식은 무엇일까요?",
        options: [
          "선택·재구성이 가능한 모듈(Module)형 구성",
          "한 번 시작하면 순서 변경이 불가능한 일방향 강의형",
          "전교생이 동일한 시험지로 치르는 일제고사형"
        ],
        answerIndex: 0,
        hint: "블록처럼 학급 상황에 맞춰 필요한 주제를 골라 조합할 수 있는 '모듈형' 구성을 떠올려 보자!"
      },
      {
        type: "ox",
        question: "4. 어울림 프로그램은 담임교사 및 교과교사 주도로 운영되며, 역할극이나 게임 등 학생 참여 중심의 다양한 방식으로 운영할 수 있다.",
        answer: "O",
        hint: "지금 우리가 함께 플레이한 시뮬레이션 게임처럼 다양한 참여형 방식으로 운영할 수 있어!"
      },
      {
        type: "text",
        question: "5. 어울림 프로그램이 기르고자 하는 '6대 핵심 역량' 중 한 가지를 정확히 적어보세요!",
        badgeText: "6대 핵심 역량 중 1가지 입력",
        answers: [
          "공감",
          "의사소통",
          "감정조절",
          "갈등해결",
          "자기존중감",
          "학교폭력인식및대처",
          "학교폭력 인식 및 대처",
          "인식및대처",
          "인식 및 대처"
        ],
        hint: "6대 핵심 역량은 ①공감, ②의사소통, ③감정조절, ④갈등해결, ⑤자기존중감, ⑥학교폭력 인식 및 대처야! 이 중 하나를 적어봐!"
      }
    ];

    function showScreen(screenId) {
      document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
      document.getElementById(screenId).classList.add("active");
    }

    function prepareTutorForStep(hintText) {
      currentHintContent = hintText;
      hasClickedTutorInStep = false;
      document.getElementById("tutorHintText").textContent = "모르는 점이 있다면 토끼선생님을 눌러서 힌트를 받아보세요!";
    }

    document.getElementById("tutorToggleBtn").addEventListener("click", () => {
      const bubble = document.getElementById("tutorBubble");
      const hintEl = document.getElementById("tutorHintText");

      if (!hasClickedTutorInStep) {
        hasClickedTutorInStep = true;
        isTutorBubbleVisible = true;
        hintEl.textContent = currentHintContent;
        bubble.style.display = "block";
      } else {
        isTutorBubbleVisible = !isTutorBubbleVisible;
        if (isTutorBubbleVisible) {
          hintEl.textContent = currentHintContent;
          bubble.style.display = "block";
        } else {
          bubble.style.display = "none";
        }
      }
    });

    document.getElementById("startBtn").addEventListener("click", () => {
      const input = document.getElementById("studentNameInput");
      const errorEl = document.getElementById("nameErrorMsg");
      const val = input.value.trim();

      if (!val) {
        errorEl.textContent = "이름을 입력해야 활동을 시작할 수 있습니다.";
        input.classList.remove("shake");
        void input.offsetWidth;
        input.classList.add("shake");
        input.focus();
        return;
      }

      studentName = val;
      errorEl.textContent = "";
      document.querySelectorAll(".user-name-slot").forEach(el => {
        el.textContent = studentName;
      });

      document.getElementById("topBar").style.display = "flex";
      openScenarioScreen(1);
    });

    document.getElementById("studentNameInput").addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        document.getElementById("startBtn").click();
      }
    });

    function openScenarioScreen(num) {
      currentScenarioNum = num;
      const sc = scenarios[num];

      document.getElementById("tutorFloatingWrap").style.display = "none";
      document.getElementById("stepLabel").textContent = sc.badge;
      document.getElementById("progressFill").style.width = num === 1 ? "12%" : "48%";

      document.getElementById("scenarioBadge").textContent = sc.badge;
      document.getElementById("scenarioTitle").textContent = sc.title;
      document.getElementById("scenarioNotiTime").textContent = sc.notiTime;
      document.getElementById("scenarioNotiBody").innerHTML = sc.notiBody.split("{name}").join(studentName);
      document.getElementById("scenarioDesc").innerHTML = sc.desc.split("{name}").join(studentName);
      document.getElementById("goStageBtn").textContent = sc.btnText;

      showScreen("screenScenario");

      const notiBox = document.getElementById("scenarioNotiBox");
      notiBox.classList.remove("noti-pop-anim");
      void notiBox.offsetWidth;
      notiBox.classList.add("noti-pop-anim");
    }

    document.getElementById("goStageBtn").addEventListener("click", () => {
      const sc = scenarios[currentScenarioNum];
      const chatArea = document.getElementById("chatArea");
      const typing = document.getElementById("typingIndicator");

      chatArea.innerHTML = "";
      const datePill = document.createElement("div");
      datePill.className = "kakao-date-pill";
      datePill.textContent = sc.datePill;
      chatArea.appendChild(datePill);

      typing.textContent = `${sc.partnerName}님이 메시지를 입력하고 있습니다...`;
      chatArea.appendChild(typing);

      document.getElementById("chatPartnerName").textContent = sc.partnerName;
      document.getElementById("tutorFloatingWrap").style.display = "flex";
      showScreen("screenChat");
      loadChatStep(0);
    });

    function loadChatStep(idx) {
      currentStepIndex = idx;
      const sc = scenarios[currentScenarioNum];
      const step = sc.steps[idx];
      const chatArea = document.getElementById("chatArea");
      const typing = document.getElementById("typingIndicator");
      const missionBox = document.getElementById("missionBox");
      const feedback = document.getElementById("missionFeedback");

      document.getElementById("stepLabel").textContent = `STAGE ${currentScenarioNum}`;
      document.getElementById("chatStageSubtitle").textContent = step.stageLabel;
      document.getElementById("progressFill").style.width = step.progress + "%";
      feedback.textContent = "";
      feedback.className = "feedback-banner";

      prepareTutorForStep(step.hint);

      if (step.isNewMessage) {
        missionBox.style.display = "none";
        typing.style.display = "block";
        chatArea.appendChild(typing);
        chatArea.scrollTop = chatArea.scrollHeight;

        setTimeout(() => {
          typing.style.display = "none";
          const formattedEn = step.enText.split("{name}").join(studentName);
          const formattedKo = step.koText.split("{name}").join(studentName);

          appendOtherMessage(formattedEn, formattedKo, step.timeLabel, sc.partnerName, sc.partnerEmoji);
          renderMission(step);
        }, 850);
      } else {
        renderMission(step);
      }
    }

    function appendOtherMessage(en, ko, timeStr, partnerName, partnerEmoji) {
      const chatArea = document.getElementById("chatArea");

      const row = document.createElement("div");
      row.className = "kakao-msg-row other";

      const avatar = document.createElement("div");
      avatar.className = "kakao-profile-pic";
      avatar.textContent = partnerEmoji;

      const col = document.createElement("div");
      col.className = "kakao-msg-col";

      const sender = document.createElement("div");
      sender.className = "kakao-sender-name";
      sender.textContent = partnerName;

      const bubbleLine = document.createElement("div");
      bubbleLine.className = "kakao-bubble-line";

      const bubble = document.createElement("div");
      bubble.className = "kakao-bubble other";
      bubble.textContent = en;

      const metaCol = document.createElement("div");
      metaCol.className = "kakao-meta-col";

      const unread = document.createElement("span");
      unread.className = "kakao-unread";
      unread.textContent = "1";

      const time = document.createElement("span");
      time.className = "kakao-time";
      time.textContent = timeStr;

      metaCol.appendChild(unread);
      metaCol.appendChild(time);

      setTimeout(() => {
        unread.style.display = "none";
      }, 700);

      bubbleLine.appendChild(bubble);
      bubbleLine.appendChild(metaCol);

      const transBtn = document.createElement("button");
      transBtn.type = "button";
      transBtn.className = "translate-btn";
      transBtn.textContent = "한글 해석 보기";

      const transDiv = document.createElement("div");
      transDiv.className = "translated-text";
      transDiv.textContent = ko;

      transBtn.addEventListener("click", () => {
        const isHidden = transDiv.style.display === "none" || transDiv.style.display === "";
        transDiv.style.display = isHidden ? "block" : "none";
        transBtn.textContent = isHidden ? "한글 해석 숨기기" : "한글 해석 보기";
        chatArea.scrollTop = chatArea.scrollHeight;
      });

      col.appendChild(sender);
      col.appendChild(bubbleLine);
      col.appendChild(transBtn);
      col.appendChild(transDiv);

      row.appendChild(avatar);
      row.appendChild(col);
      chatArea.appendChild(row);
      chatArea.scrollTop = chatArea.scrollHeight;
    }

    function appendMyMessage(text, timeStr) {
      const chatArea = document.getElementById("chatArea");

      const row = document.createElement("div");
      row.className = "kakao-msg-row me";

      const metaCol = document.createElement("div");
      metaCol.className = "kakao-meta-col";

      const unread = document.createElement("span");
      unread.className = "kakao-unread";
      unread.textContent = "1";

      const time = document.createElement("span");
      time.className = "kakao-time";
      time.textContent = timeStr;

      metaCol.appendChild(unread);
      metaCol.appendChild(time);

      const bubble = document.createElement("div");
      bubble.className = "kakao-bubble me";
      bubble.textContent = text;

      setTimeout(() => {
        unread.style.display = "none";
      }, 650);

      row.appendChild(metaCol);
      row.appendChild(bubble);
      chatArea.appendChild(row);
      chatArea.scrollTop = chatArea.scrollHeight;
    }

    function renderMission(step) {
      const sc = scenarios[currentScenarioNum];
      const missionBox = document.getElementById("missionBox");
      const titleEl = document.getElementById("missionTitle");
      const listEl = document.getElementById("optionList");
      const feedback = document.getElementById("missionFeedback");

      titleEl.textContent = step.missionTitle;
      listEl.innerHTML = "";
      missionBox.style.display = "block";

      step.options.forEach((optText, i) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "option-btn";
        btn.textContent = `${i + 1}. ${optText}`;

        btn.addEventListener("click", () => {
          if (i === step.answerIndex) {
            btn.classList.add("correct");
            feedback.className = "feedback-banner success";
            feedback.textContent = "정확합니다! 다음 단계로 이동합니다.";

            listEl.querySelectorAll(".option-btn").forEach(b => b.disabled = true);

            if (step.replyEn) {
              appendMyMessage(step.replyEn, step.timeLabel);
            }

            setTimeout(() => {
              if (currentStepIndex + 1 < sc.steps.length) {
                loadChatStep(currentStepIndex + 1);
              } else {
                showStageResult(currentScenarioNum);
              }
            }, 950);
          } else {
            btn.classList.add("wrong");
            btn.classList.remove("shake");
            void btn.offsetWidth;
            btn.classList.add("shake");
            feedback.className = "feedback-banner";
            feedback.textContent = "다시 한 번 생각해 볼까요? 우측 하단 토끼선생님을 눌러 힌트를 확인해 보세요!";
          }
        });

        listEl.appendChild(btn);
      });
    }

    function showStageResult(stageNum) {
      const sc = scenarios[stageNum];
      document.getElementById("tutorFloatingWrap").style.display = "none";
      document.getElementById("stepLabel").textContent = `STAGE ${stageNum} CLEAR`;
      document.getElementById("progressFill").style.width = stageNum === 1 ? "44%" : "73%";

      document.getElementById("stageResultBadge").textContent = sc.resultBadge;
      document.getElementById("stageResultTitle").textContent = sc.resultTitle;
      document.getElementById("stageResultSubtitle").textContent = sc.resultSubtitle;
      document.getElementById("stageResultDesc").innerHTML = sc.resultDesc.split("{name}").join(studentName);
      document.getElementById("stageResultEnglish").innerHTML = sc.resultEnglish;
      document.getElementById("stageResultTheory").innerHTML = sc.resultTheory;

      const nextBtn = document.getElementById("stageResultNextBtn");
      nextBtn.textContent = sc.resultBtnText;
      nextBtn.onclick = () => {
        if (stageNum === 1) {
          openScenarioScreen(2);
        } else {
          startQuizPhase();
        }
      };

      showScreen("screenStageResult");
    }

    function startQuizPhase() {
      document.getElementById("tutorFloatingWrap").style.display = "flex";
      isTutorBubbleVisible = true;
      document.getElementById("tutorBubble").style.display = "block";
      showScreen("screenQuiz");
      loadQuiz(0);
    }

    function loadQuiz(idx) {
      currentQuizIndex = idx;
      const q = quizData[idx];
      const progress = 75 + (idx * 5);

      document.getElementById("stepLabel").textContent = `QUIZ ${idx + 1}/5`;
      document.getElementById("progressFill").style.width = progress + "%";
      document.getElementById("quizCounter").textContent = `핵심 정리 퀴즈 ${idx + 1} / 5`;
      document.getElementById("quizQuestion").textContent = q.question;

      const feedback = document.getElementById("quizFeedback");
      feedback.textContent = "";
      feedback.className = "feedback-banner";

      prepareTutorForStep(q.hint);

      const chosungWrap = document.getElementById("quizChosungWrap");
      const optionList = document.getElementById("quizOptionList");
      const oxWrap = document.getElementById("quizOxWrap");

      chosungWrap.style.display = "none";
      optionList.style.display = "none";
      oxWrap.style.display = "none";

      if (q.type === "chosung" || q.type === "text") {
        chosungWrap.style.display = "block";
        const chosungDisplay = document.getElementById("quizChosungDisplay");
        if (q.type === "chosung") {
          chosungDisplay.style.fontSize = "28px";
          chosungDisplay.style.letterSpacing = "0.2em";
          chosungDisplay.textContent = q.chosung;
        } else {
          chosungDisplay.style.fontSize = "18px";
          chosungDisplay.style.letterSpacing = "0.02em";
          chosungDisplay.textContent = q.badgeText;
        }
        const input = document.getElementById("quizTextInput");
        input.disabled = false;
        input.value = "";
        document.getElementById("quizTextSubmitBtn").disabled = false;
        input.focus();
      } else if (q.type === "choice") {
        optionList.style.display = "flex";
        optionList.innerHTML = "";
        q.options.forEach((opt, i) => {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "option-btn";
          btn.textContent = `${i + 1}. ${opt}`;
          btn.addEventListener("click", () => {
            if (i === q.answerIndex) {
              btn.classList.add("correct");
              optionList.querySelectorAll("button").forEach(b => b.disabled = true);
              handleQuizSuccess();
            } else {
              btn.classList.add("wrong");
              btn.classList.remove("shake");
              void btn.offsetWidth;
              btn.classList.add("shake");
              feedback.className = "feedback-banner";
              feedback.textContent = "오답입니다! 정확한 정답을 선택해야 다음 문제로 넘어갈 수 있어요.";
            }
          });
          optionList.appendChild(btn);
        });
      } else if (q.type === "ox") {
        oxWrap.style.display = "grid";
        oxWrap.querySelectorAll(".ox-btn").forEach(btn => {
          btn.className = "ox-btn";
          btn.removeAttribute("style");
          btn.disabled = false;
          btn.onclick = () => {
            if (btn.dataset.ox === q.answer) {
              btn.style.borderColor = "var(--success)";
              btn.style.background = "var(--success-bg)";
              btn.style.color = "var(--success)";
              oxWrap.querySelectorAll("button").forEach(b => b.disabled = true);
              handleQuizSuccess();
            } else {
              btn.style.borderColor = "var(--danger)";
              btn.style.background = "var(--danger-bg)";
              btn.style.color = "var(--danger)";
              btn.classList.remove("shake");
              void btn.offsetWidth;
              btn.classList.add("shake");
              feedback.className = "feedback-banner";
              feedback.textContent = "오답입니다! 다시 선택해 주세요.";
            }
          };
        });
      }
    }

    document.getElementById("quizTextSubmitBtn").addEventListener("click", () => {
      const q = quizData[currentQuizIndex];
      const input = document.getElementById("quizTextInput");
      const feedback = document.getElementById("quizFeedback");
      const userAns = input.value.trim().replace(/\s+/g, "").toLowerCase();
      const validAnswers = q.answers.map(a => a.replace(/\s+/g, "").toLowerCase());

      if (validAnswers.includes(userAns)) {
        input.disabled = true;
        document.getElementById("quizTextSubmitBtn").disabled = true;
        handleQuizSuccess();
      } else {
        input.classList.remove("shake");
        void input.offsetWidth;
        input.classList.add("shake");
        feedback.className = "feedback-banner";
        feedback.textContent = "정답이 아닙니다! 초성과 토끼선생님 힌트를 보고 다시 입력해 주세요.";
      }
    });

    document.getElementById("quizTextInput").addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        document.getElementById("quizTextSubmitBtn").click();
      }
    });

    function handleQuizSuccess() {
      const feedback = document.getElementById("quizFeedback");
      feedback.className = "feedback-banner success";
      feedback.textContent = "정답입니다! 훌륭해요.";

      setTimeout(() => {
        if (currentQuizIndex + 1 < quizData.length) {
          loadQuiz(currentQuizIndex + 1);
        } else {
          finishActivity();
        }
      }, 850);
    }

    function finishActivity() {
      document.getElementById("stepLabel").textContent = "REFLECTION";
      document.getElementById("progressFill").style.width = "95%";
      document.getElementById("tutorFloatingWrap").style.display = "none";
      showScreen("screenEnding");
    }

    const STORAGE_KEY = "pov_in_your_dm_reflections_v2";

    function getReflections() {
      try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
          memoryReflections = JSON.parse(stored);
        }
      } catch (e) {}
      return memoryReflections;
    }

    function saveReflectionItem(entry) {
      const list = getReflections();
      list.unshift(entry);
      memoryReflections = list;
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
      } catch (e) {}
    }

    function launchConfetti() {
      const layer = document.getElementById("confettiLayer");
      layer.innerHTML = "";
      const colors = ["#FBE39D", "#FFD166", "#FF8FA3", "#A0C4FF", "#BDB2FF", "#CAFFBF"];

      for (let i = 0; i < 42; i++) {
        const piece = document.createElement("div");
        piece.className = "confetti-piece";
        piece.style.left = Math.random() * 100 + "%";
        piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        piece.style.animationDuration = (Math.random() * 1.8 + 1.8).toFixed(2) + "s";
        piece.style.animationDelay = (Math.random() * 0.6).toFixed(2) + "s";
        layer.appendChild(piece);
      }
    }

    document.getElementById("saveReflectionBtn").addEventListener("click", () => {
      const textarea = document.getElementById("reflectionInput");
      const feedback = document.getElementById("reflectionFeedback");
      const text = textarea.value.trim();

      if (!text) {
        feedback.className = "feedback-banner";
        feedback.textContent = "소감을 한 줄 이상 작성해 주세요.";
        textarea.focus();
        return;
      }

      const now = new Date();
      const timeStr = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")}`;

      saveReflectionItem({
        name: studentName || "참여자",
        text: text,
        time: timeStr
      });

      textarea.value = "";
      feedback.textContent = "";
      document.getElementById("topBar").style.display = "none";
      showScreen("screenMissionClear");
      launchConfetti();
    });

    const TEACHER_PASSWORD = "1234";

    function renderReflectionsList() {
      const container = document.getElementById("reflectionListContainer");
      const list = getReflections();
      container.innerHTML = "";

      if (list.length === 0) {
        container.innerHTML = `<p style="color: var(--text-muted); text-align: center; padding: 30px 0;">아직 등록된 소감이 없습니다.</p>`;
      } else {
        list.forEach(item => {
          const div = document.createElement("div");
          div.className = "reflection-item";

          const meta = document.createElement("div");
          meta.className = "reflection-meta";
          const nameSpan = document.createElement("span");
          nameSpan.textContent = item.name;
          const timeSpan = document.createElement("span");
          timeSpan.textContent = item.time;
          meta.appendChild(nameSpan);
          meta.appendChild(timeSpan);

          const body = document.createElement("div");
          body.className = "reflection-text";
          body.textContent = item.text;

          div.appendChild(meta);
          div.appendChild(body);
          container.appendChild(div);
        });
      }
    }

    function openReflectionsModal() {
      const lockBox = document.getElementById("teacherLockBox");
      const unlockedContent = document.getElementById("teacherUnlockedContent");
      const pwInput = document.getElementById("teacherPasswordInput");
      const errEl = document.getElementById("teacherAuthError");

      lockBox.style.display = "flex";
      unlockedContent.style.display = "none";
      pwInput.value = "";
      errEl.textContent = "";

      document.getElementById("reflectionModal").style.display = "flex";
      setTimeout(() => pwInput.focus(), 50);
    }

    document.getElementById("teacherUnlockBtn").addEventListener("click", () => {
      const pwInput = document.getElementById("teacherPasswordInput");
      const errEl = document.getElementById("teacherAuthError");

      if (pwInput.value === TEACHER_PASSWORD) {
        errEl.textContent = "";
        document.getElementById("teacherLockBox").style.display = "none";
        document.getElementById("teacherUnlockedContent").style.display = "flex";
        renderReflectionsList();
      } else {
        errEl.textContent = "교사 비밀번호가 일치하지 않습니다.";
        pwInput.classList.remove("shake");
        void pwInput.offsetWidth;
        pwInput.classList.add("shake");
        pwInput.focus();
      }
    });

    document.getElementById("teacherPasswordInput").addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        document.getElementById("teacherUnlockBtn").click();
      }
    });

    document.getElementById("secretTeacherBtn").addEventListener("click", openReflectionsModal);

    document.getElementById("closeModalBtn").addEventListener("click", () => {
      document.getElementById("reflectionModal").style.display = "none";
    });

    document.getElementById("copyReflectionsBtn").addEventListener("click", () => {
      const list = getReflections();
      if (list.length === 0) return;

      const formatted = list.map((item, idx) => `${idx + 1}. [${item.name}] (${item.time}) ${item.text}`).join("\n");
      const tempTextarea = document.createElement("textarea");
      tempTextarea.value = formatted;
      tempTextarea.style.position = "fixed";
      tempTextarea.style.opacity = "0";
      document.body.appendChild(tempTextarea);
      tempTextarea.select();

      try {
        document.execCommand("copy");
        const btn = document.getElementById("copyReflectionsBtn");
        btn.textContent = "클립보드에 복사 완료!";
        setTimeout(() => {
          btn.textContent = "전체 소감 복사하기";
        }, 1800);
      } catch (err) {} finally {
        document.body.removeChild(tempTextarea);
      }
    });
  </script>
</body>
</html>
"""

components.html(HTML_CONTENT, height=820, scrolling=True)
