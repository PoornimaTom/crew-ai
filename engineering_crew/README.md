# EngineeringCrew Crew

## Project Overview

EngineeringCrew Crew is a template for building multi-agent AI systems using [crewAI](https://docs.crewai.com/en/installation). This project orchestrates a team of specialized AI agents—such as architects, backend engineers, frontend engineers, and QA engineers—to collaboratively solve complex engineering tasks. Each agent is configurable and can be assigned specific roles, tools, and goals, allowing for flexible automation and intelligent task execution.

The system is designed for extensibility, making it easy to add new agents, tasks, and custom logic. You can define agent behaviors and task flows using YAML configuration files, and leverage crewAI's orchestration features to maximize productivity and collaboration.

## Installation

1. **Prerequisites:**
   - Python >=3.10 and <3.14
   - [UV](https://docs.astral.sh/uv/) for dependency management
   - (Optional) Docker, if you want agents to execute code in isolated environments

2. **Install UV:**
   ```bash
   pip install uv
   ```

3. **Install Dependencies:**
   Navigate to your project directory and run:
   ```bash
   uv pip install -r requirements.txt
   ```
   Or, if using crewAI CLI:
   ```bash
   crewai install
   ```

4. **Set up Environment Variables:**
   - Add your `OPENAI_API_KEY` to a `.env` file in the project root.

5. **Configure Agents and Tasks:**
   - Edit `src/engineering_crew/config/agents.yaml` to define your agents
   - Edit `src/engineering_crew/config/tasks.yaml` to define your tasks

## Deployment & Running

To deploy and run your crew of AI agents:

1. From the root folder, start the crew:
   ```bash
   crewai run
   ```
   This will initialize the EngineeringCrew, assemble the agents, and execute the tasks as defined in your configuration files.

2. Outputs (such as reports or results) will be generated in the project directory, as specified by your task configuration.

## Customization

- Modify `src/engineering_crew/crew.py` to add custom logic, tools, or agent/task arguments.
- Update `src/engineering_crew/main.py` to provide custom inputs or orchestrate advanced workflows.

## Documentation & Support

- [crewAI Installation Guide](https://docs.crewai.com/en/installation)
- [crewAI Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Chat with crewAI Docs](https://chat.g.pt/DWjSBZn)

## About

EngineeringCrew Crew is designed to help you harness the power of multi-agent AI collaboration for engineering and automation tasks. Get started quickly, customize to your needs, and scale your AI workflows with ease.
