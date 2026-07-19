# PRODUCT_ARCHITECTURE

Version: 0.1

## Purpose

This document describes the complete architecture of the Latenca
product.

It defines product modules, responsibilities, relationships and user
flows.

The architecture should remain stable even as individual features
evolve.

------------------------------------------------------------------------

# Product Vision

Latenca is an AI-powered wall decoration platform centered on helping
users make confident design decisions.

The core object is **a wall project**, not a product listing.

------------------------------------------------------------------------

# High-Level Architecture

    User
     │
     ▼
    Home
     │
     ├── Inspiration
     ├── Catalog
     ├── AI Designer
     └── Community
          │
          ▼
     Wall Project
          │
     ├── Artworks
     ├── Layout
     ├── Frames
     ├── Sizes
     └── Notes
          │
          ▼
     Checkout
          │
          ▼
     Learning System

------------------------------------------------------------------------

# Core Modules

## 1. Home

Purpose: - Entry point - Quick actions - Continue previous projects -
Inspire new users

KPIs: - Time to first action - AI usage rate

------------------------------------------------------------------------

## 2. Inspiration

Functions: - Featured walls - Trending layouts - Collections - Styles -
Community projects

Output: User starts a wall project.

------------------------------------------------------------------------

## 3. Catalog

Purpose: Support traditional browsing.

Functions: - Search - Filters - Categories - Collections

Must coexist with AI guidance.

------------------------------------------------------------------------

## 4. AI Designer

Purpose: Primary recommendation engine.

Responsibilities: - Understand user goals - Ask clarifying questions -
Recommend layouts - Recommend artwork - Explain recommendations -
Increase confidence

Future: Visual understanding of rooms.

------------------------------------------------------------------------

## 5. Wall Project

The central object in the system.

Contains: - Selected artworks - Layout - Room information - Sizes -
Frames - Style - AI history

Everything revolves around the wall project.

------------------------------------------------------------------------

## 6. Community

Purpose: Share completed wall designs.

Possible actions: - Publish - Like - Save - Reuse as starting point

------------------------------------------------------------------------

## 7. Checkout

Responsibilities: - Purchase artworks - Frames - Accessories

Future: Bundle optimization.

------------------------------------------------------------------------

## 8. Account

Stores: - Projects - Orders - Preferences - Saved walls

------------------------------------------------------------------------

## 9. Learning System

Collects: - Accepted recommendations - Rejected recommendations -
Purchases - User feedback

Purpose: Improve future recommendations.

------------------------------------------------------------------------

# Relationships

AI Designer creates Wall Projects.

Catalog feeds Wall Projects.

Community generates Inspiration.

Learning System improves AI Designer.

Checkout closes the loop.

------------------------------------------------------------------------

# Product States

Visitor

↓

Explorer

↓

Designer

↓

Buyer

↓

Returning Customer

↓

Advocate

------------------------------------------------------------------------

# Future Modules

-   Room Scanner
-   AR Preview
-   Team Workspace
-   Interior Designer Mode
-   Marketplace
-   API

------------------------------------------------------------------------

# Architecture Principles

1.  Wall project is the primary entity.
2.  AI assists every important decision.
3.  Every module should increase confidence.
4.  Simple user experience, powerful backend.
5.  Product should improve through real usage.
