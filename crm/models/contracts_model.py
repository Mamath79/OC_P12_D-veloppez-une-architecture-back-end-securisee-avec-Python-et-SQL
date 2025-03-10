from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from crm.database.base import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    payed_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    contract_status_id = Column(
        Integer, ForeignKey("contract_status.id", ondelete="SET NULL"), nullable=True
    )
    clients_id = Column(
        Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False
    )
    sales_contact_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime, nullable=True, onupdate=lambda: datetime.now(timezone.utc)
    )
    deleted_at = Column(DateTime, nullable=True)

    # Relations
    client = relationship("Client", back_populates="contracts", passive_deletes=True)
    status = relationship("ContractStatus", back_populates="contracts")
    invoices = relationship("Invoice", back_populates="contract")
    event = relationship("Event", back_populates="contract")
    sales_contact = relationship("User", back_populates="contracts_managed")

    def __repr__(self):
        return f"Contract(id={self.id}, Client_ID={self.clients_id}, Status_ID={self.contract_status_id or None})"
