---
title: "blogging with astro dev"
summary: "A comprehensive guide about blogging with astro dev"
date: "May 12 2025"
series: "Curriculum - AI"
draft: false
tags:
    - AI
    - CrewAI
    - Technical Guide
    
---

```bash
# Step 1: Install Astro
# Use the following command to create a new Astro project.
npm create astro@latest
```

After creating your project, navigate into the directory:

```bash
cd your-astro-project
```

### Step 2: Create Your First Post

Next, create your first Markdown post. Navigate to the `src/pages` directory and create a new file named `my-first-post.md`:

```markdown
---
title: "My First Blog Post"
description: "This is my very first post written with Astro."
pubDate: "2023-10-01"
---

# Welcome to My Blog

This is my very first post using Astro. I am excited to share my thoughts and journeys with everyone.

## Why Astro?

Astro allows for amazing performance by delivering static pages with dynamic components. It's great for bloggers who want speed and efficiency.

### Key Features
- **Fast and optimized**: Astro only delivers what is required.
- **Framework agnostic**: Use your favorite UI framework.
- **Markdown support**: Writing is simple and enjoyable.

![Astro Rocks](src/assets/astro-rocks.jpg)
```

### Step 3: Configuration

Astro uses a configuration file named `astro.config.mjs`. Here is a basic setup to define global settings:

```javascript
// src/astro.config.mjs
import { defineConfig } from 'astro/config'

export default defineConfig({
  site: 'https://your-blog-url.com',
  markdown: {
    syntaxHighlight: 'prism', // Using Prism for syntax highlighting
  },
})
```

### Step 4: Adding Components

Suppose you want to add a React component that displays a custom greeting. First, create a new component in `src/components/` named `Greeting.jsx`:

```javascript
// src/components/Greeting.jsx
import React from 'react';

const Greeting = ({ name }) => {
  return <h2>Hello, {name}! Welcome to my blog.</h2>;
};

export default Greeting;
```

Then, import and use it in your Markdown file:

```markdown
---
title: "My First Blog Post"
description: "This is my very first post written with Astro."
pubDate: "2023-10-01"
---

# Welcome to My Blog

<Greeting name="Reader" />

This is my very first post using Astro...
```

### Step 5: Building the Site

After adding your posts and components, build your site with the utility command:

```bash
# Build the project for production
npm run build
```

### Step 6: Deploying the Blog

Deploying your blog is straightforward. You can push the built files to platforms like Vercel or Netlify. Below is how it looks with Vercel:

1. Login or sign up at [Vercel](https://vercel.com/).
2. Import your GitHub repository or use the command line:
   ```bash
   vercel
   ```
3. Follow the guided prompts to deploy.

Astro also supports deployment to Netlify with simple Git integration.

### Conclusion

Congratulations! You’ve successfully set up a blog using Astro. By following these steps, you've utilized Markdown for content, embraced the flexibility of components, and poised your blog for fast load times.

### Additional Resources

- For more detailed documentation and features, visit the [Astro Documentation](https://docs.astro.build).
- Check-out community tutorials like ["Building a Blog with Astro"](https://blog.logrocket.com/building-a-blog-with-astro/) for insights and advanced techniques.

This code and setup provide a functional and insightful foundation for anyone looking to build their blog with Astro. Happy blogging!

# Commit blog article and code to git repository
git add .
git commit -m "Publish final blog article on Blogging with Astro Dev"
git push origin main