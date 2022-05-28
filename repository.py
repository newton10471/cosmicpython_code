import abc
import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        # self.session.execute('INSERT INTO ??
        print(batch.reference)
        print(batch.sku)
        print(batch._purchased_quantity)
        print(batch.eta)
        # print(batch.reference)

        self.session.execute(
            "INSERT INTO batches (reference, sku, quantity, eta) VALUES (?, ?, ?, ?)",
            batch.reference, batch.sku, batch._purchased_quantity, batch.eta)

    def get(self, reference) -> model.Batch:
        # self.session.execute('SELECT ??
        self.session.execute('SELECT reference, sku, eta from BATCHES where reference = reference')
