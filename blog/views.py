from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.responses import api_response
from .models import Blog

from django.db import transaction

from .serializers import (
    BlogResponseSerializer,
    BlogUpdateSerializer,
    BlogCreateSerializer,
)


class UserBlogView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogResponseSerializer
    queryset = Blog.objects.all()

    @swagger_auto_schema(
        operation_description="Get user blogs",
        responses={
            200: openapi.Response(
                description="Blog retrieved successfully",
                schema=BlogResponseSerializer(many=True)
            ),
            400: openapi.Response(description="Bad Request"),
            500: openapi.Response(description="Internal Server Error"),
        },
        tags=["Blogs"],
    )
    def list(self):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return api_response(
                is_success=True,
                status_code=status.HTTP_200_OK,
                result=serializer.data
            )
        except Exception as e:
            return api_response(
                is_success=False,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                result={"error": str(e)}
            )
        
class BlogCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogCreateSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        blog = serializer.save()
        return blog

    @swagger_auto_schema(
        operation_description="Create a new blog",
        request_body=BlogCreateSerializer,
        responses={
            201: openapi.Response(description="Blog created successfully"),
            400: openapi.Response(description="Bad Request"),
            500: openapi.Response(description="Internal Server Error"),
        },
        tags=["Blogs"],
    )

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(
                    is_success=True,
                    status_code=status.HTTP_201_CREATED,
                    result={"message": "Blog created successfully"}
                )
            return api_response(
                is_success=False,
                error_message=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return api_response(
                is_success=False,
                error_message=[str(e), "Internal Server Error"],
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogUpdateSerializer
    queryset = Blog.objects.all()

    @swagger_auto_schema(
        operation_description="Update an existing blog",
        request_body=BlogUpdateSerializer,
        responses={
            200: openapi.Response(description="Blog updated successfully"),
            400: openapi.Response(description="Bad Request"),
            500: openapi.Response(description="Internal Server Error"),
        },
        tags=["Blogs"],
    )
    def put(self, request):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(
                    is_success=True,
                    status_code=status.HTTP_200_OK,
                    result={"message": "Blog updated successfully"}
                )
            return api_response(
                is_success=False,
                error_message=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return api_response(
                is_success=False,
                error_message=[str(e), "Internal Server Error"],
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    @swagger_auto_schema(
        operation_description="Partially update an existing blog",
        request_body=BlogUpdateSerializer,
        responses={
            200: openapi.Response(description="Blog updated successfully"),
            400: openapi.Response(description="Bad Request"),
            500: openapi.Response(description="Internal Server Error"),
        },
        tags=["Blogs"],
    )
    def patch(self, request):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return api_response(
                    is_success=True,
                    status_code=status.HTTP_200_OK,
                    result={"message": "Blog updated successfully"}
                )
            return api_response(
                is_success=False,
                error_message=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return api_response(
                is_success=False,
                error_message=[str(e), "Internal Server Error"],
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            

class BlogDeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogResponseSerializer
    queryset = Blog.objects.all()

    @swagger_auto_schema(
        operation_description="Delete a blog",
        responses={
            204: openapi.Response(description="Blog deleted successfully"),
            400: openapi.Response(description="Bad Request"),
            500: openapi.Response(description="Internal Server Error"),
        },
        tags=["Blogs"],
    )
    def delete(self, request):
        try:
            instance = self.get_object()
            instance.delete()
            return api_response(
                is_success=True,
                status_code=status.HTTP_204_NO_CONTENT,
                result={"message": "Blog deleted successfully"}
            )
        except Exception as e:
            return api_response(
                is_success=False,
                error_message=[str(e), "Internal Server Error"],
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )