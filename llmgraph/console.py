import sys
from datetime import datetime
from time import sleep

import typer
from loguru import logger
from tqdm import tqdm
from typing_extensions import Annotated

from .library import consts, engine, env, log

typer_app = typer.Typer()


@typer_app.command()
def run(
    entity_type: Annotated[str, typer.Argument(help="Entity type (e.g. movie)")],
    entity_wikipedia: Annotated[str, typer.Argument(help="Full wikipedia link to root entity")],
    entity_root: Annotated[
        str, typer.Option(help="Optional root entity name override if different from wikipedia page title")
    ] = None,
    levels: Annotated[int, typer.Option(help="Number of levels deep to process")] = 2,
    max_sum_total_tokens: Annotated[int, typer.Option(help="Maximum sum of tokens for graph generation")] = 200000,
    output_folder: Annotated[str, typer.Option(help="Folder location to write outputs")] = "./_output/",
) -> None:
    """
    Create knowledge graphs with LLMs
    """
    if "/wiki/" in entity_type:
        raise Exception(f"You appear to have the 'entity_type' and 'entity_wikipedia' arguments mixed up.")

    custom_entity_root = True
    if "/wiki/" not in entity_wikipedia:
        raise Exception(f"{entity_wikipedia} doesn't look like a valid wikipedia url.")
    if not entity_root:
        wiki_loc = entity_wikipedia.rfind("/wiki/")
        entity_root = entity_wikipedia[wiki_loc:].replace("/wiki/", "").replace("_", " ")  # TODO: review
        custom_entity_root = False

    logger.info(f"Running with {entity_type=}, {entity_wikipedia=}, {entity_root=}, {custom_entity_root=}, {levels=}")
    if levels > 4:
        logger.warning(f"Running with {levels=} - this will take many LLM calls, watch your costs if using a paid API!")
        user_input = input(
            f"Running with {levels=} - this will take many LLM calls, watch your costs if using a paid API! Press Y to continue..."
        )
        if user_input.lower() != "y":
            sys.exit("User did not press Y.")
    start = datetime.now()
    engine.create_company_graph(entity_type, entity_root, entity_wikipedia, levels, max_sum_total_tokens, output_folder)
    took = datetime.now() - start
    logger.info(f"Done, took {took.total_seconds()}s")


# if __name__ == "__main__":
#     log.configure()
#     typer_app()
