FROM python:3.11.7
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD python -m agents.tool_maker.unit_manager
