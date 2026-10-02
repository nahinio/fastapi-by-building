## Arcade Armor
When players enter the lobby inside a retro RPG arcade zone, available weapons, potions, and armor must render instantly. Arcade Armor requires an ultra-fast, read-only menu & inventory API so game can fetch the latest gear listings. 

## Core Deliverables:
 - Zero-Latency In-Memory Reads: Store and serve catalog items directly from memory.
 - Full Inventory Retrieval: Return structured lists of all available equipment.
 - Dynamic Category Filtering: Query items by class (e.g., armor, weapon, potion, accessory).
 - Single-Item Lookup: Fetch item stats and availability by unique item ID with proper 404 Not Found handling.
 - Strict Response Validation: Enforce consistent JSON response formats using Pydantic schemas.

## Architecture
```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#2b2b2b",
  "primaryTextColor": "#ffffff",
  "primaryBorderColor": "#888888",
  "lineColor": "#888888",
  "textColor": "#ffffff",
  "edgeLabelBackground": "#2b2b2b",
  "clusterBkg": "transparent",
  "clusterBorder": "#888888",
  "titleColor": "#888888"
}}}%%
flowchart LR

    subgraph C["Client"]
        CR["Client Request"]
    end

    API["FastAPI Server"]

    subgraph D["Data & Response"]
        Memory["In-Memory Armor Data"]
        JSON["JSON Response"]
    end

    subgraph E["API Operations"]
        All["List All Armor Items"]
        Category["Filter Armor by Category"]
        Single["Get Single Armor Item"]
    end

    CR --> API

    API --> Memory
    API --> JSON

    API -->|"GET /armor-items"| All
    API -->|"GET /armor-items?category=weapon"| Category
    API -->|"GET /armor-items/{id}"| Single

    classDef node fill:#2b2b2b,stroke:#888888,stroke-width:1px,color:#ffffff
    classDef core fill:#2b2b2b,stroke:#cccccc,stroke-width:2px,color:#ffffff

    class CR,Memory,JSON,All,Category,Single node
    class API core

    style C fill:transparent,stroke:#888888,stroke-width:1px,stroke-dasharray:4 4,color:#888888
    style D fill:transparent,stroke:#888888,stroke-width:1px,stroke-dasharray:4 4,color:#888888
    style E fill:transparent,stroke:#888888,stroke-width:1px,stroke-dasharray:4 4,color:#888888

    linkStyle default stroke:#888888,stroke-width:1px
```