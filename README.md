# llmgraph

[![PyPI version](https://badge.fury.io/py/llmgraph.svg?1)](https://badge.fury.io/py/llmgraph)
[![build](https://github.com/dylanhogg/llmgraph/actions/workflows/python-poetry-app.yml/badge.svg)](https://github.com/dylanhogg/llmgraph/actions/workflows/python-poetry-app.yml)
[![Latest Tag](https://img.shields.io/github/v/tag/dylanhogg/llmgraph)](https://github.com/dylanhogg/llmgraph/tags)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/llmgraph/blob/master/notebooks/llmgraph_example.ipynb)

<!-- [![Dependencies](https://img.shields.io/librariesio/github/dylanhogg/llmgraph)](https://libraries.io/github/dylanhogg/llmgraph) -->

Create knowledge graphs with LLMs.

![example machine learning output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/header.jpg?raw=true)

llmgraph enables you to create knowledge graphs in [GraphML](http://graphml.graphdrawing.org/), [GEXF](https://gexf.net/), and HTML formats (generated via [pyvis](https://github.com/WestHealth/pyvis)) from a given source entity Wikipedia page. The knowledge graphs are generated by extracting world knowledge from ChatGPT or other large language models (LLMs) as supported by [LiteLLM](https://github.com/BerriAI/litellm).

For a background on knowledge graphs see a [youtube overview by Computerphile](https://www.youtube.com/watch?v=PZBm7M0HGzw)

## Features

- Create knowledge graphs, given a source entity.
- Uses ChatGPT (or another specified LLM) to extract world knowledge.
- Generate knowledge graphs in HTML, GraphML, and GEXF formats.
- Many entity types and relationships supported by [customised prompts](https://github.com/dylanhogg/llmgraph/blob/main/llmgraph/prompts.yaml).
- Cache support to iteratively grow a knowledge graph, efficiently.
- Outputs `total tokens` used to understand LLM costs (even though a default run is only about 1 cent).
- Customisable model (default is OpenAI `gpt-3.5-turbo` for speed and cost).

## Installation

You can install llmgraph using pip, ideally into a Python [virtual environment](https://realpython.com/python-virtual-environments-a-primer/#create-it):

```bash
pip install llmgraph
```

Alternatively, checkout [an example notebook](https://github.com/dylanhogg/llmgraph/blob/main/notebooks/llmgraph_example.ipynb) that uses llmgraph and you can run directly in Google Colab.

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/llmgraph/blob/master/notebooks/llmgraph_example.ipynb)

## Example Output

In addition to GraphML and GEXF formats, an HTML [pyvis](https://github.com/WestHealth/pyvis) physics enabled graph can be viewed:

### Artificial Intelligence example

![example machine-learning output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/machine-learning_artificial-intelligence_v1.0.0_level4_fully_connected.png?raw=true)
<sub>Generate above machine-learning graph:<br />`llmgraph machine-learning "https://en.wikipedia.org/wiki/Artificial_intelligence" --levels 4`
<br />View entire graph: <a target="_blank" href="https://blog.infocruncher.com/html/llmgraph/machine-learning_artificial-intelligence_v1.0.0_level4_fully_connected.html">machine-learning_artificial-intelligence_v1.0.0_level4_fully_connected.html</a></sub>

## llmgraph Usage

### Example Usage

The example above was generated with the following command, which requires an `entity_type` and a quoted `entity_wikipedia` souce url:

```bash
llmgraph machine-learning "https://en.wikipedia.org/wiki/Artificial_intelligence" --levels 3
```

This example creates a 3 level graph, based on the given start node `Artificial Intelligence`.

By default OpenAI is used and you will need to set an environment variable '`OPENAI_API_KEY`' prior to running. See the [OpenAI docs](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key) for more info. The `total tokens used` is output as the run progresses. For reference this 3 level example used a total of 7,650 gpt-3.5-turbo tokens, which is approx 1.5 cents as of Oct 2023.

You can also specify a different LLM provider, including running with a local [ollama](https://github.com/jmorganca/ollama) model. You should be able to specify anything supported by [LiteLLM](https://github.com/BerriAI/litellm) as described here: https://docs.litellm.ai/docs/providers. Note that the prompts to extract related entities were tested with OpenAI and may not work as well with other models.

Local [ollama/llama2](https://ollama.ai/library/llama2) model example:

```bash
llmgraph machine-learning "https://en.wikipedia.org/wiki/Artificial_intelligence" --levels 3 --llm-model ollama/llama2 --llm-base-url http://localhost:<your_port>
```

The `entity_type` sets the LLM prompt used to find related entities to include in the graph. The full list can be seen in [prompts.yaml](https://github.com/dylanhogg/llmgraph/blob/main/llmgraph/prompts.yaml) and include the following entity types:

- `automobile`
- `book`
- `computer-game`
- `concepts-general`
- `creative-general`
- `documentary`
- `food`
- `machine-learning`
- `movie`
- `music`
- `people-historical`
- `podcast`
- `software-engineering`
- `tv`

### Required Arguments

- `entity_type` (TEXT): Entity type (e.g. movie)
- `entity_wikipedia` (TEXT): Full Wikipedia link to the root entity

### Optional Arguments

- `--entity-root` (TEXT): Optional root entity name override if different from the Wikipedia page title [default: None]
- `--levels` (INTEGER): Number of levels deep to construct from the central root entity [default: 2]
- `--max-sum-total-tokens` (INTEGER): Maximum sum of tokens for graph generation [default: 200000]
- `--output-folder` (TEXT): Folder location to write outputs [default: ./_output/]
- `--llm-model` (TEXT): The model name [default: gpt-3.5-turbo]
- `--llm-temp` (FLOAT): LLM temperature value [default: 0.0]
- `--llm-base-url` (TEXT): LLM will use custom base URL instead of the automatic one [default: None]
- `--version`: Display llmgraph version and exit.
- `--help`: Show this message and exit.

## More Examples of HTML Output

Here are some more examples of the HTML graph output for different entity types and root entities (with commands to generate and links to view full interactive graphs).

Install llmgraph to create your own knowledge graphs! Feel free to share interesting results in the [issue section](https://github.com/dylanhogg/llmgraph/issues/new) above with a documentation label :)

### Knowledge graph concept example

![example concepts-general output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/concepts-general_knowledge-graph_v1.0.0_level4_fully_connected.png?raw=true)
<sub>Command to generate above concepts-general graph:<br />`llmgraph concepts-general "https://en.wikipedia.org/wiki/Knowledge_graph" --levels 4`
<br />View entire graph: <a target="_blank" href="https://blog.infocruncher.com/html/llmgraph/concepts-general_knowledge-graph_v1.0.0_level4_fully_connected.html">concepts-general_knowledge-graph_v1.0.0_level4_fully_connected.html</a></sub>

### Inception movie example

![example movie output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/movie_inception_v1.0.0_level4_fully_connected.png?raw=true)
<sub>Command to generate above movie graph:<br />`llmgraph movie "https://en.wikipedia.org/wiki/Inception" --levels 4`
<br />View entire graph: <a target="_blank" href="https://blog.infocruncher.com/html/llmgraph/movie_inception_v1.0.0_level4_fully_connected.html">movie_inception_v1.0.0_level4_fully_connected.html</a></sub>

### OpenAI company example

![example company output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/company_openai_v1.0.0_level4_fully_connected.png?raw=true)
<sub>Command to generate above company graph:<br />`llmgraph company "https://en.wikipedia.org/wiki/OpenAI" --levels 4`
<br />View entire graph: <a target="_blank" href="https://blog.infocruncher.com/html/llmgraph/company_openai_v1.0.0_level4_fully_connected.html">company_openai_v1.0.0_level4_fully_connected.html</a></sub>

### John von Neumann people example

![example people-historical output](https://github.com/dylanhogg/llmgraph/blob/main/docs/img/people-historical_john-von-neumann_v1.0.0_level4_fully_connected.png?raw=true)
<sub>Command to generate above people-historical graph:<br />`llmgraph people-historical "https://en.wikipedia.org/wiki/John_von_Neumann" --levels 4`
<br />View entire graph: <a target="_blank" href="https://blog.infocruncher.com/html/llmgraph/people-historical_john-von-neumann_v1.0.0_level4_fully_connected.html">people-historical_john-von-neumann_v1.0.0_level4_fully_connected.html</a></sub>

## Example of Prompt Used to Generate Graph

Here is an example of the prompt template, with place holders, used to generate related entities from a given source entity. This is applied recursively to create a knowledge graph, merging duplicated nodes as required.

```
You are knowledgeable about {knowledgeable_about}.
List, in json array format, the top {top_n} {entities} most like '{{entity_root}}'
with Wikipedia link, reasons for similarity, similarity on scale of 0 to 1.
Format your response in json array format as an array with column names: 'name', 'wikipedia_link', 'reason_for_similarity', and 'similarity'.
Example response: {{{{"name": "Example {entity}","wikipedia_link": "https://en.wikipedia.org/wiki/Example_{entity_underscored}","reason_for_similarity": "Reason for similarity","similarity": 0.5}}}}
```

It works well on the primary tested LLM, being OpenAI gpt-3.5-turbo. Results are ok, but not as good using Llama2. The prompt source of truth and additional details can be see in [prompts.yaml](https://github.com/dylanhogg/llmgraph/blob/main/llmgraph/prompts.yaml).

Each entity type has custom placeholders, for example `concepts-general` and `documentary`:

```
concepts-general:
    system: You are a highly knowledgeable ontologist and creator of knowledge graphs.
    knowledgeable_about: many concepts and ontologies.
    entities: concepts
    entity: concept name
    top_n: 5

documentary:
    system: You are knowledgeable about documentaries of all types, and genres.
    knowledgeable_about: documentaries of all types, and genres
    entities: Documentaries
    entity: Documentary
    top_n: 5
```

## Cached LLM API calls

Each call to the LLM API (and Wikipedia) is cached locally in a `.joblib_cache` folder. This allows an interrupted run to be resumed without duplicating identical calls. It also allows a re-run with a higher `--level` option to re-use results from the lower level run (assuming the same entity type and source).

## Future Improvements

- Contrast graph output from different LLM models (e.g. [Llama2](https://huggingface.co/docs/transformers/model_doc/llama2) vs [Mistral](https://huggingface.co/docs/transformers/model_doc/mistral) vs [ChatGPT-4](https://openai.com/chatgpt))
- Investigate the hypothosis that this approach provides insight into how an LLM views the world.
- Include more examples in this documentation and make examples available for easy browsing.
- Instructions for running locally and adding a custom `entity_type` prompt.
- Better pyviz html output, in particular including reasons for entity relationship in UI and arguments for pixel size etc.
- Parallelise API calls and result processing.
- Remove dependency on Wikipedia entities as a source.
- Contrast results from llmgraphg with other non-LLM graph construction e.g. using wikipedia page links, or [direct article embeddings](https://txt.cohere.com/embedding-archives-wikipedia/).

## Contributing

Contributions to llmgraph are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Create a pull request with a description of your changes.

## Thanks 🙏

Thanks to @breitburg for implementing the LiteLLM updates.

## References

- https://arxiv.org/abs/2211.10511 - Knowledge Graph Generation From Text
- https://arxiv.org/abs/2310.04562 - Towards Foundation Models for Knowledge Graph Reasoning
- https://arxiv.org/abs/2206.14268 - BertNet: Harvesting Knowledge Graphs with Arbitrary Relations from Pretrained Language Models
- https://github.com/aws/graph-notebook - Graph Notebook: easily query and visualize graphs
- https://github.com/KiddoZhu/NBFNet-PyG - PyG re-implementation of Neural Bellman-Ford Networks
- https://caminao.blog/knowledge-management-booklet/a-hitchhikers-guide-to-knowledge-galaxies/ - A Hitchhiker’s Guide to Knowledge Galaxies
