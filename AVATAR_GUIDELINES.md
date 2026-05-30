# Personal Board of Directors - Avatar Design & Generation Guidelines

To maintain a consistent, ultra-premium, and artistically unified user interface, all board member avatars must follow the custom **"Sketch-Watercolor" (素描彩绘)** style. 

This document defines the visual standards, generation prompts, and integration workflow for adding or updating board member portraits in the future.

---

## 🎨 1. Visual Style Standard

The visual anchor for all board members is the hand-drawn sketch of **Warren Buffett**:
* **Medium**: Pencil/ink line drawing with gray wash watercolor shading.
* **Outlines**: Fine, elegant black ink contours.
* **Shading**: Delicate pencil cross-hatching combined with smooth, soft grayscale watercolor washes. No harsh shadows or saturated colors.
* **Background**: Solid, pure white (`#FFFFFF`) to blend seamlessly with the light-mode UI and glassmorphism elements.
* **Composition**: Centered portrait, friendly and professional expression, eyes looking slightly towards the viewer.

---

## ✍️ 2. Avatar Generation Prompt

When generating a new board member's portrait (e.g., using AI image generators), use the following highly-specified prompt structure. You **must** provide the existing `buffett.png` or `munger.png` as a style reference image (`ImagePaths`).

### Prompt Template:
```text
A high-quality artistic sketch portrait of [PERSON_NAME]. Follow the style of the reference image: a clean, elegant hand-drawn line art sketch with fine black ink outlines, delicate cross-hatching, and subtle gray-scale watercolor wash shading for depth. The portrait is centered, friendly, looking slightly towards the viewer, on a solid pure white background. Minimalist, premium, professional editorial illustration style, identical artistic medium and sketch drawing technique as the reference image.
```

*Replace `[PERSON_NAME]` with the actual name, and optionally append specific physical traits if necessary (e.g., `"wearing glasses"` for Charlie Munger).*

---

## 📁 3. File System & Naming Conventions

All avatars must be saved locally to prevent CORS errors, broken hotlinks, or slow page load times.

* **Target Directory**: `frontend/src/assets/`
* **Filename Standard**: `[member_id].png`
  - Example: `munger.png`
  - Example: `buffett.png`
  - Example: `graham.png`

---

## 💻 4. Code Integration

When adding a member to the board, import the asset statically at the top of [App.tsx](file:///c:/Users/17968/AI%20projects/Personal%20Board/frontend/src/App.tsx) and assign it to the `BOARD_MEMBERS` array:

```typescript
// 1. Import the asset
import newMemberPhoto from './assets/new_member.png';

// 2. Add to BOARD_MEMBERS array
const BOARD_MEMBERS = [
  ...
  { 
    id: 'new_member', 
    name: 'New Member Name', 
    title: 'Their Title', 
    photo: newMemberPhoto, 
    color: 'text-indigo-600', 
    border: 'border-indigo-400', 
    ring: 'ring-indigo-200' 
  },
];
```

---

## 🚀 5. Existing Assets Inventory

The following matched portraits are currently generated and active in the system:
* **Warren Buffett** (`buffett.png`) - *The master reference style*
* **Charlie Munger** (`munger.png`) - *Matching style generated on May 30, 2026*
* **Paul Graham** (`graham.png`) - *Matching style generated on May 30, 2026*
