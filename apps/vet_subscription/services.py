from .repositories import VetSubscriptionRepository

class OwnerService:
    @staticmethod
    def list_vet_subscriptions():
        return VetSubscriptionRepository.get_all()

    @staticmethod
    def create_vet_subscription(data):
        return VetSubscriptionRepository.create(data)

    @staticmethod
    def delete_vet_subscription(vet_subscription_id):
        return VetSubscriptionRepository.delete(vet_subscription_id)
