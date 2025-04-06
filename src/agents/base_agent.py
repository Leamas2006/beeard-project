import os
import random
import time
from abc import ABC, abstractmethod


class BaseSearchAgent(ABC):
    def __init__(self, query, agent_id, output_dir):
        self.query = query
        self.agent_id = agent_id
        self.output_dir = output_dir
        self.results = []

    @abstractmethod
    def search(self):
        """Выполнить поиск по запросу"""
        pass

    @abstractmethod
    def download(self, item):
        """Скачать найденный ресурс"""
        pass

    def save_results(self):
        """Сохранить результаты поиска"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # Логика сохранения
